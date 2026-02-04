import pandas as pd
import matplotlib.pyplot as plt

# Load ECG data
df = pd.read_csv("data/processed/100.csv")

# Use first ECG lead
signal = df.iloc[:, 0]

# Moving average window size (baseline estimation)
window_size = 200

# Estimate baseline
baseline = signal.rolling(window=window_size, center=True).mean()

# Remove baseline
ecg_corrected = signal - baseline

# Plot comparison
plt.figure()

plt.plot(signal[:2000], label="Raw ECG", alpha=0.6)
plt.plot(ecg_corrected[:2000], label="Baseline Removed ECG")

plt.title("Baseline Wander Removal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()

plt.show()
