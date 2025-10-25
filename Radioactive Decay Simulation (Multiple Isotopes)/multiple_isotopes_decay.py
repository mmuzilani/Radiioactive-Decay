"""
Radioactive Decay Simulation (Multiple Isotopes)
Author: Md. Mahiuddin Zilani
Description: Simulates and compares radioactive decay of multiple isotopes on the same graph.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Input Section
# -----------------------------
num_isotopes = int(input("Enter number of isotopes to simulate: "))
isotopes = []

for i in range(num_isotopes):
    name = input(f"Name of isotope {i+1} (e.g., C-14): ")
    N0 = int(input(f"Initial number of nuclei for {name}: "))
    half_life = float(input(f"Half-life of {name} (seconds): "))
    isotopes.append({"name": name, "N0": N0, "half_life": half_life})

time_steps = int(input("Enter number of time steps: "))
time_max = max([iso['half_life'] for iso in isotopes]) * 10
time = np.linspace(0, time_max, time_steps)

# -----------------------------
# Calculations and Plotting
# -----------------------------
plt.figure(figsize=(10,6))

for iso in isotopes:
    decay_constant = np.log(2) / iso['half_life']
    N = iso['N0'] * np.exp(-decay_constant * time)
    plt.plot(time, N, label=f"{iso['name']} (Half-life: {iso['half_life']} s)")

plt.xlabel('Time (s)')
plt.ylabel('Number of Nuclei')
plt.title('Radioactive Decay: Multiple Isotopes Comparison')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig('Multiple_Isotopes_Comparison.png')
plt.show()
