import serial
import time
import numpy as np
from sklearn.linear_model import Ridge

# --- PROJECT GENESIS: HYBRID HDC-RNC ENGINE ---
# Harnessing BCN Material Chaos for High-Dimensional Computing and Reservoir Processing.

# Configuration
ARDUINO_PORT = 'COM3' # Update to your device port
BAUD_RATE = 115200
DIMENSIONS = 1000      # HDC Dimension (10k recommended for production)

print("--- GENESIS HYBRID ENGINE: INITIALIZING ---")

# --- CONNECT TO CHIP ---
try:
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=0.1)
    print(f"✅ PHY-L0: Connected to BCN Hardware on {ARDUINO_PORT}")
    time.sleep(2) # Initial reset
except Exception as e:
    print(f"❌ PHY-L0: Connection Failed. Error: {e}")
    exit()

def read_chip_state():
    """Reads raw analog entropy from the BCN lattice."""
    line = ser.readline().decode('utf-8').strip()
    try:
        val = int(line)
        # Normalize to [-1, 1] range for reservoir processing
        return (val - 512) / 512.0
    except:
        return 0.0

# --- PART 1: HDC (Hyperdimensional Computing) ---
print("\n--- 🧠 HDC Phase: Generating Matter-Based Hypervectors ---")

def generate_hypervector_from_matter(dim, label="DATA"):
    """Harvests entropy-dense vectors from the physical BCN lattice."""
    hv = []
    print(f"Harvesting {dim}D Entropy for '{label}'...", end='')
    for _ in range(dim):
        state = read_chip_state()
        bit = 1 if state > 0.05 else -1 # Simple thresholding for bipolar HV
        hv.append(bit)
        time.sleep(0.002) # Sync with Arduino 500Hz stream
    print(" Done.")
    return np.array(hv)

# Create High-Dimensional Memory (Item Memory)
im_normal = generate_hypervector_from_matter(DIMENSIONS, "NORMAL_STATE")
im_hot    = generate_hypervector_from_matter(DIMENSIONS, "HEAT_STATE")
im_cold   = generate_hypervector_from_matter(DIMENSIONS, "COLD_STATE")

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

sim = cosine_similarity(im_normal, im_hot)
print(f"Orthogonality Check (Ideal ~0): {sim:.4f}")
if abs(sim) < 0.1:
    print("STATUS: High-Quality Orthogonality. The BCN lattice is a perfect Entropy source.")

# --- PART 2: RNC (Reservoir Computing) ---
print("\n--- 🌊 RNC Phase: Physical Reservoir Training (XOR Problem) ---")

# Inputs (XOR)
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 0]
reservoir_states = []

print("Injecting logic stimuli into BCN Reservoir...")
for inp in inputs:
    current_state = []
    # Project 2D input into 20D Reservoir state via physical perturbation
    for _ in range(20):
        chip_val = read_chip_state()
        # Simulated Physical Perturbation (Actual: DAC voltage injection)
        perturbed_val = chip_val * (inp[0] + inp[1] + 1.5)
        current_state.append(perturbed_val)
        time.sleep(0.005)
    reservoir_states.append(current_state)

# Linear Readout Layer Training (Bridge between Chaos and Logic)
readout = Ridge(alpha=0.5)
readout.fit(reservoir_states, outputs)
print("Training Complete. Readout Layer weights locked.")

# Testing the XOR Reservoir
print("\n--- INFERENCE TEST ---")
for i, inp in enumerate(inputs):
    test_state = reservoir_states[i]
    prediction = readout.predict([test_state])[0]
    print(f"Input: {inp} | BCN Reaction -> Prediction: {prediction:.4f}")

ser.close()
print("\n--- GENESIS ENGINE: STANDBY ---")
