import pandas as pd
import matplotlib.pyplot as plt

# Load the ECG CSV file
df = pd.read_csv("data/processed/100.csv")

# Plot only first 2000 samples to keep it clear
plt.figure()
plt.plot(df.iloc[:2000, 0])

plt.title("Raw ECG Signal (Noisy)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

plt.show()
