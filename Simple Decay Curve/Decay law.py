# Radioactive Decay Simulation

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# User inputs
# -----------------------------
N0 = int(input("Enter initial number of nuclei (N0): "))
half_life = float(input("Enter half-life (in seconds): "))
time_steps = int(input("Enter number of time steps: "))

# -----------------------------
# Calculations
# -----------------------------
decay_constant = np.log(2) / half_life  # Decay constant λ
time = np.linspace(0, half_life*10, time_steps)  # Time array
N = N0 * np.exp(-decay_constant * time)  # Number of nuclei at each time

# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(time, N, 'b-', label='Nuclei remaining')
plt.xlabel('Time (s)')
plt.ylabel('Number of nuclei')
plt.title('Radioactive Decay Simulation')
plt.grid(True)
plt.legend()
plt.show()
# Save 7
plt.savefig('Decay Curve.png')

