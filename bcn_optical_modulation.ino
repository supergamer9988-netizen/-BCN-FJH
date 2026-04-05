// GENESIS: OPTICAL MODULATOR
// Purpose: Control Laser Intensity (PWM) for BCN Chip stimulation.
// Connection: Pin 9 -> Laser Module (+), GND -> Laser Module (-)

const int LASER_PIN = 9;

void setup() {
  Serial.begin(115200);
  pinMode(LASER_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    
    // Manual Level Control (Example: L:128)
    if (cmd.startsWith("L:")) {
      int level = cmd.substring(2).toInt();
      analogWrite(LASER_PIN, constrain(level, 0, 255));
      Serial.print("LASER_INTENSITY:");
      Serial.println(level);
    }
  }
  
  // Auto-Pulse Simulation (Data Injection Mode)
  // Low -> Med -> High -> Off
  simulate_photon_injection();
}

void simulate_photon_injection() {
  for(int i=0; i<=255; i+=51) {
    analogWrite(LASER_PIN, i);
    delay(200);
  }
  analogWrite(LASER_PIN, 0);
  delay(1000);
}
