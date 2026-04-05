import numpy as np
import matplotlib.pyplot as plt
import serial
import time

# --- PROJECT GENESIS: BUTTERFLY LOOP ANALYZER (V 1.0) ---
# Purpose: Detect Bipolar Switching (Figure-8) in BCN Memristors.
# Searching for the "Crossover Point" where the UP and DOWN curves intersect.

SERIAL_PORT = 'COM3' # Update to your device!
BAUD_RATE = 115200

def capture_sweep():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
        time.sleep(2)
        
        up_curve = []
        down_curve = []
        
        print("--- [BUTTERFLY ANALYZER : STARTING SWEEP] ---")
        
        # We assume the Arduino is streaming "UP,X,Y" and "DOWN,X,Y"
        # from the Calibration Sketch.
        
        timeout_limit = time.time() + 10 # 10 second capture
        while time.time() < timeout_limit:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("UP"):
                parts = line.split(",")
                up_curve.append((int(parts[1]), int(parts[2])))
            elif line.startswith("DOWN"):
                parts = line.split(",")
                down_curve.append((int(parts[1]), int(parts[2])))
                
            if len(up_curve) >= 50 and len(down_curve) >= 50:
                break

        ser.close()
        return np.array(up_curve), np.array(down_curve)

    except Exception as e:
        print(f"Blink Error: {e}")
        return None, None

def analyze_butterfly(up, down):
    if up is None or down is None: return
    
    # 1. Normalize for Comparison
    x_up, y_up = up[:,0], up[:,1]
    x_down, y_down = down[:,0], down[:,1]
    
    # Sort Down curve to align with Up X-axis
    idx = np.argsort(x_down)
    x_down_sorted, y_down_sorted = x_down[idx], y_down[idx]
    
    # 2. Search for Intersections (The Butterfly Point)
    diff = y_up - np.interp(x_up, x_down_sorted, y_down_sorted)
    zero_crossings = np.where(np.diff(np.sign(diff)))[0]
    
    print("\n--- [ANALYSIS RESULT] ---")
    
    # Exclude endpoints (0 and 255)
    valid_crossings = [idx for idx in zero_crossings if 10 < x_up[idx] < 245]
    
    if len(valid_crossings) > 0:
        print(f"✅ BUTTERFLY DETECTED! (Bipolar Switching Found)")
        print(f"Crossover Point: X={x_up[valid_crossings[0]]} | Y={y_up[valid_crossings[0]]}")
        print("Status: NON-VOLATILE MEMORY CAPABLE (GOD TIER)")
    else:
        print("⚠️ OVAL LOOP DETECTED (Unipolar Switching)")
        print("Status: SHORT-TERM MEMORY ONLY (RESERVOIR GRADE)")

    # 3. Plot for Visualization
    plt.figure(figsize=(10,6))
    plt.plot(x_up, y_up, label='UP (Increasing)', color='cyan', linewidth=2)
    plt.plot(x_down, y_down, label='DOWN (Decreasing)', color='gold', linewidth=2)
    plt.title("BCN Memristor: Hysteresis Butterfly Analysis")
    plt.xlabel("Stimulus Intensity (PWM)")
    plt.ylabel("Material Response (AnalogRead)")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    up, down = capture_sweep()
    analyze_butterfly(up, down)
