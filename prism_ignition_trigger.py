import serial
import time

# --- PRISM IGNITION CONTROL SCRIPT ---
# This script controls an Arduino/ESP32 to trigger the Flash Joule Heating pulse
# and read the resistance value from the BCN chip post-flash.

# Configuration
SERIAL_PORT = 'COM3'   # Update this to your MCU's port
BAUD_RATE = 115200
FLASH_DELAY = 2.0      # Seconds to wait before checking resistance

def trigger_ignition():
    try:
        # Initialize Serial Connection
        print(f"Connecting to {SERIAL_PORT}...")
        mc = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        time.sleep(2) # Give MCU time to reset
        
        print("--- PRISM SYSTEM READY ---")
        print("Preparing for Flash Joule Heating (FJH)...")
        input("PRESS ENTER TO TRIGGER IGNITION (DANGEROUS: STAND BACK!)")
        
        # Send Trigger Signal
        print("Command: FLASH_START")
        mc.write(b'F') # Sending 'F' character to trigger relay
        
        # Wait for the explosion/pulse to complete
        print("FLASHING...")
        time.sleep(FLASH_DELAY)
        
        # Request Resistance Reading
        print("Command: READ_RESISTANCE")
        mc.write(b'R') # Sending 'R' to read ADC
        
        # Read the response
        response = mc.readline().decode('utf-8').strip()
        print(f">> INITIAL RESISTANCE: {response} Ohms")
        
        if "ERROR" in response:
            print("System Warning: Ignition incomplete or short circuit detected.")
        else:
            print("System Success: BCN Lattice stabilized. Ready for Prism.Map().")
            
        mc.close()

    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    trigger_ignition()
