# ☢️ Radioactive Decay Simulation (Multiple Isotopes)


## 📘 Description

This Python program **simulates and compares the radioactive decay** of multiple isotopes on the same graph.  
Each isotope’s decay is modeled using the **exponential decay law**:

\[
N(t) = N_0 e^{-\lambda t}
\]

where  
- \( N_0 \) → Initial number of nuclei  
- \( \lambda = \frac{\ln(2)}{\text{Half-life}} \) → Decay constant  
- \( t \) → Time  
- \( N(t) \) → Number of nuclei remaining after time \( t \)

---

## ⚙️ Features

✨ Simulate **any number of isotopes** (e.g., C-14, U-238, Na-23)  
📈 Plots all decay curves on the **same graph** for easy comparison  
🧮 Automatically adjusts the **time range** based on the largest half-life  
💾 Saves the result as a **PNG image** (`Multiple_Isotopes_Comparison.png`)  


---

## 🧠 How It Works

1. The program asks for:
   - Number of isotopes to simulate  
   - Name, initial number of nuclei, and half-life for each isotope  
2. It calculates the decay constant \( \lambda \) for each isotope.  
3. It computes the number of remaining nuclei \( N(t) \) over time.  
4. It plots all decay curves together using `matplotlib`.

---

## 🧩 Example Input
Number of isotopes to simulate: 2
Name of isotope 1 (e.g., C-14): Ac-225
Initial number of nuclei for Ac-225: 1000
Half-life of Ac-225 (seconds): 10
Name of isotope 2 (e.g., C-14): Th-228
Initial number of nuclei for Th-228: 500
Half-life of Th-228 (seconds): 10
Number of time steps: 100


---

## 📊 Example Output

🖼️ **Generated Plot:**  
Each isotope appears with a unique color and label (half-life shown in seconds).

The figure is automatically saved as:

Multiple_Isotopes_Comparison.png


---

## 🧰 Requirements

Make sure you have the following installed:

```bash
pip install numpy matplotlib

🚀 How to Run

Run the script in your Python IDE or terminal:
python multiple_isotopes_decay.py

⭐ If you like this project, consider giving it a star on GitHub!

### 🧑‍🔬 Author: **Md. Mahiuddin Zilani**

---

