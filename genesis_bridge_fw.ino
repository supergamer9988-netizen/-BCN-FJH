// GENESIS BRIDGE FIRMWARE (HDC-RNC MODE)
// Purpose: Stream high-frequency raw jitter from BCN for HDC harvesting.
// Frequency: ~500Hz samples for entropy collection.

const int BCN_PIN = A0;
const int LED_STATUS = 13;

void setup() {
  Serial.begin(115200); // High speed for HDC/RNC data density
  pinMode(LED_STATUS, OUTPUT);
}

void loop() {
  // Read BCN raw analog value (0-1023)
  int val = analogRead(BCN_PIN);
  
  // Direct stream for Python harvester
  Serial.println(val);
  
  // Status blink (5Hz)
  digitalWrite(LED_STATUS, (millis() / 200) % 2); 
  
  // 2ms delay for 500Hz sampling
  delay(2); 
}
