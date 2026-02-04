import pandas as pd
import matplotlib.pyplot as plt

# Load raw ECG
raw_df = pd.read_csv("data/processed/100.csv")
raw_signal = raw_df.iloc[:, 0]

# Load cleaned ECG
cleaned_df = pd.read_csv("data/cleaned/100_cleaned.csv")
cleaned_signal = cleaned_df["ECG_Cleaned"]

# Plot comparison
plt.figure()

plt.plot(raw_signal[:2000], label="Raw ECG", alpha=0.6)
plt.plot(cleaned_signal[:2000], label="Cleaned ECG")

plt.title("Raw ECG vs Cleaned ECG")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()

plt.show()
