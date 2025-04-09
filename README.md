# 📡 RF Modulation Classification & Communication System Simulation

## 🚀 Bridging Deep Learning & Wireless Communication
This project presents an intelligent, end-to-end system that leverages deep learning to classify RF modulation schemes and transmit synthetic I/Q data in real time. Using a CLDNN model trained on the **RadioML 2016.10A** dataset, the system dynamically predicts modulation types and transmits newly generated signals via UDP between devices. It brings together communication theory, signal processing, and neural networks to simulate the future of **cognitive radio** and **adaptive wireless systems**.

---

## 📌 Project Workflow

1.  **Classify RF signals** using a trained CLDNN model (Conv1D + LSTM + Dense layers).
2.  **Generate synthetic I/Q samples** dynamically based on predicted modulation.
3.  **Transmit the I/Q samples** to another system using UDP protocol.
4.  **Receive and visualize the I/Q constellation** using a Python GUI.
5.  **Evaluate modulation effectiveness** using signal plots and prediction validation.

---

## 📂 Dataset: RadioML 2016.10A

The dataset contains:
- 220,000 samples of RF signals.
- Each sample is a 2×128 array (In-phase and Quadrature).
- Modulations: BPSK, QPSK, 8PSK, 16QAM, 64QAM, CPFSK, GFSK, PAM4, etc.
- SNR range: -20 dB to +18 dB.

---

## 🪧 Data Preprocessing

-  Normalize I/Q samples per sample.
-  Encode modulation labels using `LabelEncoder`.
-  Train-validation-test split (e.g., 70-15-15).

---

## 🧐 Deep Learning Model: CLDNN
**CLDNN (Convolutional + LSTM + Dense Neural Network)** is used for effective time-domain signal classification.

### Architecture:
- `Conv1D` layers to extract temporal features.
- `BatchNormalization` to stabilize training.
- `LSTM` to capture sequence dependencies.
- `Dense` layers with dropout for classification.

### Output:
- Trained to classify 8–11 modulation types.
- Accuracy ~63% (baseline, tunable).

### Export:
- Model saved as `.h5` and converted to `.onnx` for cross-platform deployment.

---

## 🌌 Synthetic I/Q Data Generation
- Generates new I/Q samples for: BPSK, QPSK, 8PSK, 16QAM, 64QAM, PAM4, GFSK, CPFSK.
- Ensures no reuse of training input for transmission.
- Power-normalized for consistency across modulation types.

---

## 🚬 Real-time Communication via UDP

### Sender:
- Predicts modulation.
- Generates synthetic I/Q.
- Transmits via UDP to target IP.

### Receiver:
- Listens on specified port.
- GUI built with `Tkinter + Matplotlib`.
- Displays I/Q constellation on signal arrival.

---

## 🎡 Applications
- Cognitive radio networks
- IoT communication simulators
- Secure wireless experimentation
- Adaptive modulation switching

---

## 🚀 Future Enhancements
- Real SDR (Software Defined Radio) hardware integration.
- Auto-tuning of hyperparameters.
- AI-guided modulation adaptation based on channel conditions.
- SNR estimation + BER evaluation module.

---

## 📚 License
This project is licensed under the MIT License.

---

### 📢 Let's redefine wireless communication with AI!

