// Simple Arduino transmitter sketch to send sensor data over Serial
const int SENSOR_PIN = A0;  // Analog pin for sensor (e.g., temperature sensor)
const int BAUD_RATE = 9600; // Serial communication baud rate

void setup() {
  // Initialize serial communication
  Serial.begin(BAUD_RATE);
  while (!Serial) {
    ; // Wait for serial port to connect (needed for some boards)
  }
  Serial.println("Arduino Transmitter Initialized");
}

void loop() {
  // Read sensor value (e.g., temperature)
  int sensorValue = analogRead(SENSOR_PIN);
  
  // Convert to a meaningful unit (e.g., voltage or temperature)
  float voltage = sensorValue * (5.0 / 1023.0); // Assuming 5V reference
  
  // Send data as a simple JSON-like string
  Serial.print("{\"sensor\":\"temperature\",\"value\":");
  Serial.print(voltage);
  Serial.println("}");

  // Delay for 1 second before next reading
  delay(1000);
}