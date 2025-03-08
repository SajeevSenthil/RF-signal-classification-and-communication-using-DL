# **📡 RF Modulation Classification & Communication System Simulation**

🚀 **Bridging Machine Learning & Wireless Communication!** 🚀\
This project fuses **deep learning** with **real-time RF communication**, creating an intelligent system that **classifies RF signals and transmits synthetic I/Q data dynamically**. From **CNN-based modulation recognition** to **wireless data transmission**, this work explores the future of cognitive radio and adaptive communications.

---

## **📌 Project Overview**

This project follows a structured approach:

1️⃣ **Classify RF signals** using deep learning (CNN model trained on RadioML 2018.01A dataset of 18GB).\
2️⃣ **Generate synthetic I/Q samples** in MATLAB for transmission.\
3️⃣ **Dynamically select modulation schemes based on the classified signal output to optimize transmission.**\
4️⃣ Transmit & receive modulated RF signals between two systems. \
5️⃣ **Apply modulation, encoding, and decoding** to reconstruct transmitted data.

🔹 **Applications:** Adaptive modulation, cognitive radio, IoT, and secure wireless networks.

---

## **📂 Dataset: [RadioML 2018.01A](https://f002.backblazeb2.com/file/deepsig-datasets/2018.01/2018.01.OSC.0001_1024x2M.h5.tar.gz?Authorization=3_20250307172457_4c985cf1a825131c9e63406e_7c912e72741a8c9ca16e3d7a466674b54efc1d15_002_20250307182457_0042_dnld)**

📊 **Dataset Includes:**

- **2 million samples of 1024-length I/Q data** representing modulated RF signals.
- **Modulation labels** (BPSK, QPSK, 8PSK, 16QAM, 64QAM, etc.).
- **Various SNR levels**, simulating real-world wireless conditions.

🛠 **Preprocessing Steps:**

✅ Normalization of I/Q data.\
✅ Label encoding for deep learning models.\
✅ Splitting into training, validation, and test sets.

---

## **🧠 Deep Learning for RF Classification**

🎯 **Why CNNs?**

- Extracts key features from I/Q sequences.
- Handles noisy RF signals efficiently.
- Enables real-time classification with high accuracy.

📌 **Training Workflow:**

1️⃣ Train a **1D CNN** on RadioML 2018.01A.\
2️⃣ Export the trained model in **ONNX format** for MATLAB integration.\
3️⃣ Use the model to classify real or simulated RF signals.

---

## **📡 Generating Synthetic I/Q Data**

📌 **Why Generate New Data?**

- The classification model **does not reuse input signals for transmission**.
- Instead, we create **fresh I/Q samples** to modulate and send new messages.

🔹 **Steps:**

✅ Generate **random binary data**.

✅ Convert to **I/Q format** based on modulation type.

✅ Structure data for **RF transmission**.

---

## **📡 Transmission Between Two Laptops**

1️⃣ **Software-Based Transmission (TCP/UDP)**: Send modulated I/Q data over a network.

🔹 **Key Components:**

✅ **Sender:** Modulates & transmits RF signals.

✅ **Receiver:** Receives & demodulates signals to extract original data.

✅ **Noise Simulation:** Introduces **AWGN & fading** to mimic real-world conditions.

---

## **🎯 Modulation, Encoding & Decoding**

📌 **The Heart of Wireless Communication!**

- **Modulation:** Converts bits to RF signals (BPSK, QPSK, 16-QAM, etc.).
- **Encoding:** Maps bits into symbols for error resilience.
- **Decoding & Demodulation:** Recovers transmitted data at the receiver.
- **BER Analysis:** Computes Bit Error Rate to measure transmission quality.

---

## **🚀 Final Thoughts**

This project successfully integrates **deep learning-based RF classification** with **real-time transmission**, bridging the gap between **ML & communication systems**. Future enhancements include:
✅ **Real SDR implementation** for live RF experiments.\
✅ **More advanced modulation techniques** for high-efficiency transmission.\
✅ **AI-driven adaptive modulation** based on channel conditions.

📢 **Let's redefine wireless communication with AI!**

