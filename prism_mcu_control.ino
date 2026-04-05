// PRISM MCU CONTROL BOOTLOADER
// Hardware: Arduino Uno/Nano, Relay Module, ADC Bridge
// Purpose: Trigger FJH and Measure Resistance

const int RELAY_PIN = 7;      // Pin connected to the FJH Relay
const int SENSOR_PIN = A0;    // Pin to read resistance across the chip
const int PULSE_MS = 100;     // Pulse duration in milliseconds

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // Safe state
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    
    if (cmd == 'F') { // TRIGGER FLASH
      digitalWrite(RELAY_PIN, HIGH);
      delay(PULSE_MS);
      digitalWrite(RELAY_PIN, LOW);
      Serial.println("FLASH_COMPLETE");
    } 
    
    if (cmd == 'R') { // READ RESISTANCE
      int val = analogRead(SENSOR_PIN);
      float resistance = mapFloat(val, 0, 1023, 0.0, 1000.0); // Simple bridge map
      Serial.print("INITIAL_RESISTANCE: ");
      Serial.println(resistance);
    }
  }
}

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
