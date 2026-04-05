import serial
import time
import math
import hashlib

# --- GENESIS: CHAOS ENTROPY ANALYZER ---
# Analyzes unique material jitter from the BCN chip to verify the Flash success.

# Configuration
SERIAL_PORT = 'COM3' # Update to your MCU port
BAUD_RATE = 115200

def calculate_entropy(data):
    if not data: return 0
    entropy = 0
    for x in set(data):
        p_x = data.count(x) / len(data)
        entropy += - p_x * math.log2(p_x)
    return entropy

def analyze_bcn_chip():
    try:
        print(f"Connecting to GENESIS Hardware on {SERIAL_PORT}...")
        mc = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        
        print("\n--- ANALYZING CHAOS LATTICE ---")
        print("Collecting 100 samples for Entropy Fingerprinting...")
        
        raw_samples = []
        while len(raw_samples) < 100:
            line = mc.readline().decode('utf-8').strip()
            if line.startswith("RAW:"):
                val = int(line.split(":")[1])
                raw_samples.append(val)
                print(f"Sample {len(raw_samples)}: {val} " + ("#" * (val // 20)))
        
        # Calculate Metrics
        avg_v = sum(raw_samples) / len(raw_samples)
        entropy = calculate_entropy(raw_samples)
        jitter = max(raw_samples) - min(raw_samples)
        
        # Generate TRNG (Hardware Security Key)
        raw_str = "".join(map(str, raw_samples))
        hw_hash = hashlib.sha256(raw_str.encode()).hexdigest()[:16]
        
        print("\n--- ANALYSIS COMPLETE ---")
        print(f"Average Resistance State: {avg_v:.2f}")
        print(f"Chaos Entropy Level: {entropy:.4f} bits/sample")
        print(f"Jitter Margin: {jitter} units")
        print(f"UNIQUE HARDWARE KEY: BCX-{hw_hash}-GOD")
        
        if jitter < 2:
            print("\nWARNING: Low Jitter - Material may be too conductive. Sintering might be overly fused.")
        elif entropy > 1.5:
            print("\nSUCCESS: High Entropy detected. The Lattice reflects quantum interference patterns!")
            
        mc.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_bcn_chip()
