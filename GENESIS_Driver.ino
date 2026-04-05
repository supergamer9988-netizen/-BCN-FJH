// GENESIS DRIVER V1.0 - OPTICAL BRIDGE
// Purpose: Interface between Python (Brain) and BCN Chip (Hardware)
// Protocols: Serial (115200bps) 
// Input: Integer (0-255) -> Laser Intensity
// Output: "DATA,VAL" -> BCN Response

const int laserPin = 9;   // Laser PWM (Photons)
const int chipPin = A0;   // BCN Resistance (Electrons)
const int ledStatus = 13; // Built-in LED

void setup() {
  Serial.begin(115200);   // High-speed data link
  pinMode(laserPin, OUTPUT);
  pinMode(ledStatus, OUTPUT);
  analogWrite(laserPin, 0); // Start in standby
}

void loop() {
  if (Serial.available() > 0) {
    // 1. Receive Stimulus from Python
    int intensity = Serial.parseInt();
    
    // Clear newline/extra chars
    while (Serial.available() > 0) Serial.read();

    // 2. Inject Photons into BCN Lattice
    analogWrite(laserPin, intensity);
    
    // 3. Physical Settling Time (Allow Hysteresis/Memory Effect to manifest)
    delay(20); 
    
    // 4. Capture Non-linear Reaction
    int reaction = analogRead(chipPin);
    
    // 5. Echo back for Reservoir Computing Analysis
    Serial.print("DATA,");
    Serial.println(reaction);
    
    // 6. Visual Sync
    digitalWrite(ledStatus, !digitalRead(ledStatus));
  }
}
