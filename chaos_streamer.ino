// CHAOS ANALYZER: High-Speed Raw Streamer
// Purpose: Send raw analog data from BCN chip to Python for Entropy analysis
// Hardware: Arduino Uno + BCN Chip (Voltage Divider)

const int BCN_PIN = A0;

void setup() {
  Serial.begin(115200); // High speed for jitter analysis
  pinMode(BCN_PIN, INPUT);
}

void loop() {
  // Read raw 10-bit value
  int rawValue = analogRead(BCN_PIN);
  
  // Output format: RAW:VAL (for Python parser)
  Serial.print("RAW:");
  Serial.println(rawValue);
  
  // High frequency sampling
  delay(5); 
}
