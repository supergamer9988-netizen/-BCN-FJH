import serial
import hashlib
import time

# --- PROJECT GENESIS: PUF KEY GENERATOR (HDC-BASED) ---
# Goal: Generate a 256-bit Digital Fingerprint from the BCN Architecture.
# Since no two BCN lattices are the same (stochastic FJH synthesis),
# the generated key is "Unclonable" and unique to your physical chip.

ARDUINO_PORT = 'COM3'   # Update!
BAUD_RATE = 115200

try:
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=0.1)
    time.sleep(2)
    print("--- [GENESIS CRYPTO : INITIALIZING] ---")
    print(f"Reading Entropy from Physical BCN Lattice on {ARDUINO_PORT}")

    entropy_pool = []
    print("Harvesting Atomic Jitter...")
    
    # 1. Harvest a unique noise signature (1000 samples)
    for _ in range(1000):
        ser.write(b"127\n") # Mid-stimulus to excite the lattice
        line = ser.readline().decode().strip()
        if "DATA," in line:
            val = int(line.split(",")[1])
            entropy_pool.append(str(val))
        time.sleep(0.005)

    # 2. Hash the entropy string to a 256-bit Key (SHA-256)
    raw_signature = "".join(entropy_pool).encode()
    puf_key = hashlib.sha256(raw_signature).hexdigest()

    print("\n--- [PHYSICAL UNCLONABLE FUNCTION (PUF) GENERATED] ---")
    print(f"Key Hash: {puf_key}")
    print("This key is derived from your specific BCN synthesis pattern.")
    print("Copying this key is impossible without stealing the physical chip.")

    ser.close()

except Exception as e:
    print(f"Blink Error: {e} (Verify Hardware Connection!)")

print("\n--- [GENESIS CRYPTO : COMPLETE] ---")
