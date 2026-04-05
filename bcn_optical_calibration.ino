// GENESIS: OPTICAL HYSTERESIS CALIBRATION (V 1.0)
// Purpose: Measure the "Memory Effect" of the BCN chip.
// If the UP curve and DOWN curve don't match (forming a loop), 
// it proves the chip is MEMRISTIVE.

const int laserPin = 9;   // Laser PWM (Photons)
const int sensorPin = A0; // BCN Resistance (Electrons)

void setup() {
  Serial.begin(9600);
  pinMode(laserPin, OUTPUT);
}

void loop() {
  // Phase 1: Ramp Up (Increasing Stimulus)
  for (int i = 0; i <= 255; i += 5) {
    analogWrite(laserPin, i);
    delay(30); // Allow lattice settling time
    int val = analogRead(sensorPin);
    
    // Output format: MODE, INPUT_INTENSITY, OUTPUT_RESPONSE
    Serial.print("UP,");
    Serial.print(i);
    Serial.print(",");
    Serial.println(val);
  }

  // Phase 2: Ramp Down (Decreasing Stimulus)
  for (int i = 255; i >= 0; i -= 5) {
    analogWrite(laserPin, i);
    delay(30);
    int val = analogRead(sensorPin);
    
    Serial.print("DOWN,");
    Serial.print(i);
    Serial.print(",");
    Serial.println(val);
  }
  
  delay(2000); // Wait between cycles
}
