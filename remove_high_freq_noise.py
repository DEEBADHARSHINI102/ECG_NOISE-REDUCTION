import pandas as pd
import matplotlib.pyplot as plt

# Load ECG data
df = pd.read_csv("data/processed/100.csv")

# Use first ECG lead
signal = df.iloc[:, 0]

# -------- Step 1: Baseline removal (same as before) --------
baseline = signal.rolling(window=200, center=True).mean()
ecg_no_baseline = signal - baseline

# -------- Step 2: Remove high-frequency noise (smoothing) --------
# Moving average smoothing
smooth_window = 10
ecg_smoothed = ecg_no_baseline.rolling(
    window=smooth_window, center=True
).mean()

# -------- Plot comparison --------
plt.figure()

plt.plot(ecg_no_baseline[:2000], label="Baseline Removed ECG", alpha=0.6)
plt.plot(ecg_smoothed[:2000], label="After High-Frequency Noise Removal")

plt.title("High-Frequency Noise Removal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()

plt.show()

# -------- Save cleaned ECG --------

# Create output folder if not exists
import os
os.makedirs("data/cleaned", exist_ok=True)

# Save cleaned signal to CSV
cleaned_df = pd.DataFrame({
    "ECG_Cleaned": ecg_smoothed
})

cleaned_df.to_csv("data/cleaned/100_cleaned.csv", index=False)

print("✅ Cleaned ECG saved to data/cleaned/100_cleaned.csv")

