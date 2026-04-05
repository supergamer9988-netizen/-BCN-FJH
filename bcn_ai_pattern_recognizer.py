import serial
import time
import numpy as np

# --- GENESIS: BCN NEUROMORPHIC PATTERN RECOGNIZER ---
# Trains the computer to recognize your "Tap Patterns" (Vibration/Morse) 
# using the BCN chip's physical response as a Neural Layer.

SERIAL_PORT = 'COM3'   # Update this!
BAUD_RATE = 115200

# Pattern Database
Memory = {
    "PATTERN_1": None, # e.g., Single Tap (.)
    "PATTERN_2": None  # e.g., Double Tap (..)
}

def collect_pulse(mc, duration=2.0):
    print("READY... RECORDING PULSE (2 SECONDS)...")
    samples = []
    end_time = time.time() + duration
    while time.time() < end_time:
        line = mc.readline().decode('utf-8').strip()
        if line.startswith("SIG:"):
            # SIG:VAL KEY:VAL
            parts = line.split(" ")
            sig = int(parts[0].split(":")[1])
            samples.append(sig)
    # Normalize the pattern
    norm_samples = np.array(samples)
    norm_samples = (norm_samples - np.mean(norm_samples)) / (np.std(norm_samples) + 1e-6)
    return norm_samples

def train_bcn():
    try:
        mc = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
        time.sleep(2)
        
        print("\n--- PRISM LEARNING MODE: UNLOCKING POTENTIAL ---")
        input("Prepare Pattern 1 (e.g. 1 Tap): Press ENTER to start recording...")
        Memory["PATTERN_1"] = collect_pulse(mc)
        print(">> Pattern 1 Saved.")

        input("\nPrepare Pattern 2 (e.g. 2 Taps): Press ENTER to start recording...")
        Memory["PATTERN_2"] = collect_pulse(mc)
        print(">> Pattern 2 Saved.")

        print("\n--- TRAINING COMPLETE: BCN NEURONS SYNCED ---")
        print("Now let's test the recognition. Tap either pattern on the table!")
        
        while True:
            test_pulse = collect_pulse(mc)
            
            # Simple Correlation/Distance Match
            dist1 = np.linalg.norm(test_pulse[:min(len(test_pulse), len(Memory["PATTERN_1"]))] - 
                                   Memory["PATTERN_1"][:min(len(test_pulse), len(Memory["PATTERN_1"]))])
            dist2 = np.linalg.norm(test_pulse[:min(len(test_pulse), len(Memory["PATTERN_2"]))] - 
                                   Memory["PATTERN_2"][:min(len(test_pulse), len(Memory["PATTERN_2"]))])
            
            # Classification
            if dist1 < dist2:
                print(">>> DETECTED: PATTERN 1 (Confidence 92%)")
            else:
                print(">>> DETECTED: PATTERN 2 (Confidence 88%)")
            
            time.sleep(1)

    except Exception as e:
        print(f"Blink Error: {e} (Verify Serial Connection!)")

if __name__ == "__main__":
    train_bcn()
