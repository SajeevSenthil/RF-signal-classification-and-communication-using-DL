import socket
import threading
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------------- DEMODULATION FUNCTIONS -----------------
def demodulate_bpsk(iq):
    return (iq[0] > 0).astype(np.uint8)

def demodulate_qpsk(iq):
    i, q = iq[0], iq[1]
    bits = []
    for x, y in zip(i, q):
        bits.append(0 if x > 0 and y > 0 else 1 if x < 0 and y > 0 else 2 if x < 0 and y < 0 else 3)
    bits = np.array(bits, dtype=np.uint8)
    return np.unpackbits(bits[:, np.newaxis], axis=1)[:, -2:].flatten()

def demodulate_8psk(iq):
    angles = np.angle(iq[0] + 1j * iq[1])  # [-π, π]
    angles = (angles + 2 * np.pi) % (2 * np.pi)  # Ensure positive
    symbols = np.floor(angles / (2 * np.pi / 8)).astype(np.uint8) % 8
    bits = np.unpackbits(symbols[:, np.newaxis], axis=1)[:, -3:]
    return bits.flatten()

def demodulate_qam(iq, levels):
    re, im = iq[0], iq[1]
    scale = 2 * (levels // 2 - 1)
    re_levels = np.round((re + scale) / 2).astype(int)
    im_levels = np.round((im + scale) / 2).astype(int)
    re_levels = np.clip(re_levels, 0, levels - 1)
    im_levels = np.clip(im_levels, 0, levels - 1)
    symbols = re_levels * levels + im_levels
    bits_per_symbol = int(np.log2(levels * levels))
    return np.unpackbits(symbols[:, np.newaxis].astype(np.uint8), axis=1)[:, -bits_per_symbol:].flatten()

def demodulate(iq, mod_type):
    mod_type = mod_type.upper()
    if mod_type == "BPSK": return demodulate_bpsk(iq)
    if mod_type == "QPSK": return demodulate_qpsk(iq)
    if mod_type == "8PSK": return demodulate_8psk(iq)
    if mod_type == "16QAM": return demodulate_qam(iq, 4)
    if mod_type == "64QAM": return demodulate_qam(iq, 8)
    print("⚠ Demodulation not supported:", mod_type)
    return np.array([], dtype=np.uint8)

# ----------------- MAIN RECEIVER GUI -----------------
def start_tcp_receiver_gui(port=5050):
    def listen_tcp():
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("0.0.0.0", port))
            server.listen(1)
            status_label.config(text="📡 TCP Listening...")
            conn, addr = server.accept()
            data = b""
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                data += chunk
            conn.close()
            server.close()

            mod_len = data[0]
            mod_type = data[1:1+mod_len].decode()
            bit_data = data[1+mod_len:257+mod_len]
            iq_data = data[257+mod_len:]

            bits = np.frombuffer(bit_data, dtype=np.uint8)
            iq = np.frombuffer(iq_data, dtype=np.float32)

            if len(iq) % 2 != 0:
                print("⚠ Incomplete IQ pair, dropping last sample")
                iq = iq[:-1]

            iq = iq.reshape(2, -1)

            recovered = demodulate(iq, mod_type)
            min_len = min(len(bits), len(recovered))
            errors = np.sum(bits[:min_len] != recovered[:min_len])
            ber = errors / min_len if min_len > 0 else 1.0

            print("🔍 IQ shape:", iq.shape)
            print("🔓 Recovered bits:", recovered[:10])

            root.after(0, lambda: update_gui(addr, iq, mod_type, ber, errors, min_len))

        except Exception as e:
            print("❌ Error receiving TCP data:", e)

    def update_gui(addr, iq, mod, ber, err, total):
        status_label.config(
            text=f"📥 {iq.shape[1]} samples from {addr[0]}\nBER: {ber:.4f} | Errors: {err}/{total}"
        )
        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(iq[0], iq[1], s=5)
        ax.set_title(f"📡 Received I/Q Constellation ({mod})")
        ax.set_xlabel("In-phase (I)")
        ax.set_ylabel("Quadrature (Q)")
        ax.grid(True)
        ax.axis("equal")
        canvas.draw()

    def stop_app():
        root.destroy()

    # GUI setup
    root = tk.Tk()
    root.title("TCP RF Signal Receiver GUI with BER")
    root.geometry("720x620")

    status_label = ttk.Label(root, text="Waiting...", font=("Arial", 14))
    status_label.pack(pady=10)

    fig = Figure(figsize=(6.5, 5), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    ttk.Button(root, text="Start TCP Listening", command=lambda: threading.Thread(target=listen_tcp, daemon=True).start()).pack(pady=5)
    ttk.Button(root, text="Stop", command=stop_app).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_tcp_receiver_gui()
