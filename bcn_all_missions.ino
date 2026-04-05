// GENESIS: ALL-IN-ONE MISSION CODES
// Missions: 1 (Breath Test), 2 (Chaos Key), 3 (Reservoir Patterns)

const int BCN_PIN = A0;

void setup() {
  Serial.begin(115200); // High speed for jitter/pattern analysis
  pinMode(BCN_PIN, INPUT);
  
  // Mission 2: Random Seed from hardware noise
  randomSeed(analogRead(0));
}

void loop() {
  // Read Raw Value (Mission 1 & 3)
  int rawVal = analogRead(BCN_PIN);
  
  // Mission 2: Generate Chaos Key part
  unsigned long entropy = (rawVal * micros()) % 1000;
  
  // Output format for Serial Plotter and Python Parser
  // SIG: Raw Signal for plots
  // KEY: TRNG Entropy for keys
  Serial.print("SIG:");
  Serial.print(rawVal);
  Serial.print(" KEY:");
  Serial.println(entropy);
  
  // Mission 3: Sampling rate for vibration/waves
  delay(10); 
}
