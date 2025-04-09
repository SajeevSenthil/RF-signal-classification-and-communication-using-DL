import socket
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def udp_receiver_gui(port=5005, expected_samples=1024):
    def listen_and_plot():
        # Show listening status
        status_label.config(text="Listening for data...")

        # Receive data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", port))
        data, addr = sock.recvfrom(expected_samples * 2 * 4)
        sock.close()

        # Convert data
        iq = np.frombuffer(data, dtype=np.float32).reshape(2, -1)

        # Update status
        status_label.config(text=f"Received {iq.shape[1]} samples from {addr[0]}")

        # Plot
        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(iq[0], iq[1], s=5)
        ax.set_title("Received I/Q Constellation")
        ax.set_xlabel("In-phase (I)")
        ax.set_ylabel("Quadrature (Q)")
        ax.grid(True)
        ax.axis("equal")
        canvas.draw()

    def stop_app():
        root.destroy()

    # --- UI Setup ---
    root = tk.Tk()
    root.title("RF Signal Receiver GUI")
    root.geometry("700x600")

    # Status Label
    status_label = ttk.Label(root, text="Waiting to start...", font=("Arial", 14))
    status_label.pack(pady=10)

    # Plot Figure
    fig = Figure(figsize=(6, 5), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Control Buttons
    ttk.Button(root, text="Start Listening", command=listen_and_plot).pack(pady=5)
    ttk.Button(root, text="Stop Listening", command=stop_app).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    udp_receiver_gui()