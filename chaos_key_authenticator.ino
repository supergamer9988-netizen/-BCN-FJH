// CHAOS KEY: Hardware Fingerprint Authenticator
// Hardware: Arduino Uno + BCN Chip + 10k Resistor
// Circuit: 
// [5V] ---- [BCN Chip] ---- (A0) ---- [10k Resistor] ---- [GND]

const int SENSOR_PIN = A0;
const int CHALLENGE_PIN = 12; // Optional: Send pulse to BCN
const int TOLERANCE = 15;     // Sensitivity margin for authentication
const int SAVED_KEY = 450;    // Simulating a stored "Fingerprint" value

void setup() {
  pinMode(CHALLENGE_PIN, OUTPUT);
  Serial.begin(115200);
  Serial.println("--- CHAOS KEY SYSTEM: READY ---");
  Serial.println("Status: Waiting for Chip Connection...");
}

void loop() {
  // 1. Send Challenge Pulse (Optional)
  digitalWrite(CHALLENGE_PIN, HIGH);
  delay(100);
  
  // 2. Read Response from BCN (Chaos Response)
  int readVal = analogRead(SENSOR_PIN);
  float voltage = readVal * (5.0 / 1023.0);
  
  // 3. Display Raw Jitter Data (For Visualization)
  Serial.print("RAW_JITTER: ");
  Serial.print(readVal);
  Serial.print(" | VOLTS: ");
  Serial.println(voltage);

  // 4. Authentication Logic
  if (abs(readVal - SAVED_KEY) < TOLERANCE) {
    Serial.println(">> [ACCESS GRANTED]: Hardware Fingerprint Match!");
  } else if (readVal > 20) { // Check if chip is actually connected
    Serial.println(">> [ACCESS DENIED]: Unknown Hardware Signature.");
  }
  
  digitalWrite(CHALLENGE_PIN, LOW);
  delay(1000); // 1-second check interval
}
