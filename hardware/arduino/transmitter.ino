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

#Integra più sensori, come un sensore di temperatura (LM35) e un sensore di umidità (DHT11).#

    
#include <SoftwareSerial.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define LM35_PIN A0

SoftwareSerial bluetoothSerial(10, 11); // RX | TX
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    bluetoothSerial.begin(9600);
    dht.begin();
}

void loop() {
    // Leggi dati sensori
    float temperatureLM35 = analogRead(LM35_PIN) * 0.48876; // Converti in °C
    float temperatureDHT = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Invia dati via Bluetooth
    bluetoothSerial.print("TEMP_LM35:");
    bluetoothSerial.println(temperatureLM35);
    bluetoothSerial.print("TEMP_DHT:");
    bluetoothSerial.println(temperatureDHT);
    bluetoothSerial.print("HUMID:");
    bluetoothSerial.println(humidity);

    delay(2000); // Ritardo per evitare sovraccarico
}

  
### **4.2. Gestione Avanzata degli Errori**###

#Aggiungi un sistema di gestione degli errori per la connessione Bluetooth.#

  void checkBluetoothConnection() {
    if (!bluetoothSerial.available()) {
        Serial.println("Errore connessione Bluetooth");
        bluetoothSerial.println("Errore connessione Bluetooth");
    }
}

void loop() {
    checkBluetoothConnection();
    // Leggi e invia dati sensori
    // ...
}

  // Delay for 1 second before next reading
  delay(1000);
}
