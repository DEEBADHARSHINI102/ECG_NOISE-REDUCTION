# ECG Noise Reduction and Signal Enhancement

A complete and reproducible project that demonstrates **ECG signal noise reduction** using classical signal processing techniques.  
The project focuses on cleaning raw ECG signals by removing baseline wander and high-frequency (muscle) noise while preserving essential cardiac features such as the **QRS complex**.

This repository is designed to be **beginner-friendly**, **academically solid**, and **open-source ready**.

---

## 📌 Project Motivation

Electrocardiogram (ECG) signals are highly sensitive to noise introduced during acquisition. Common causes include:

- Patient movement
- Muscle activity (EMG noise)
- Respiration (baseline wander)
- Poor electrode contact
- Mobile or low-cost recording environments

Noisy ECG signals can lead to **misinterpretation and incorrect diagnosis**.  
This project demonstrates how **classical preprocessing techniques** can significantly improve ECG signal quality before further analysis or clinical use.

---

## 🧠 What This Project Does

✔ Uses real ECG data  
✔ Visualizes raw noisy ECG  
✔ Removes baseline wander  
✔ Removes high-frequency (muscle) noise  
✔ Saves cleaned ECG separately  
✔ Compares raw vs cleaned signals visually  

No artificial intelligence is used in this version — the focus is on **core signal processing fundamentals**.

---

## 📂 Dataset Used

- **MIT-BIH Arrhythmia Database**
- Source: PhysioNet
- Record used: `100`

### Files:
- `100.dat` — raw ECG signal (binary)
- `100.hea` — signal metadata

The dataset is publicly available and widely used in academic research.

---


---

## 🔬 Methods Used

### 1️⃣ Baseline Wander Removal
- Baseline estimated using a moving average filter
- Low-frequency drift removed by subtraction
- Eliminates artifacts caused by respiration and motion

### 2️⃣ High-Frequency Noise Removal
- Moving average smoothing applied
- Reduces muscle (EMG) noise
- Preserves sharp QRS complexes and ECG morphology

---

## 📊 Results

- Significant reduction in baseline drift
- High-frequency noise visibly suppressed
- ECG waveform centered and cleaner
- Essential cardiac features preserved
- Clear visual improvement confirmed through comparison plots

---




🔮 Future Enhancements

1.AI-based ECG denoising (CNN / Autoencoders)

2.Multi-lead ECG processing

3.Real-time ECG noise reduction

4.Web-based ECG visualization dashboard

## 🧪 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install wfdb numpy pandas matplotlib

