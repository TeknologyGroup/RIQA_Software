#include <SoftwareSerial.h>

// Pin per HM-10 (TXD -> 10, RXD -> 11)
SoftwareSerial bleSerial(10, 11); // RX | TX
const int LED_PIN = 13;           // LED su pin 13
const int SENSOR_PIN = A0;        // Sensore analogico su A0

void setup() {
  Serial.begin(9600);         // Seriale per debug
  bleSerial.begin(9600);      // Seriale per HM-10
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  
  // Configurazione iniziale HM-10 (opzionale)
  bleSerial.print("AT+NAME=RIQA_BLE"); // Imposta nome
  delay(100);
  bleSerial.print("AT+ROLE0");         // Modalità periferica
  delay(100);
  Serial.println("HM-10 Pronto");
}

void loop() {
  // Ricezione comandi dall'app
  if (bleSerial.available()) {
    char command = bleSerial.read();
    if (command == '1') {
      digitalWrite(LED_PIN, HIGH);
      bleSerial.println("LED ON");
    } else if (command == '0') {
      digitalWrite(LED_PIN, LOW);
      bleSerial.println("LED OFF");
    }
  }

  // Invio dati sensore ogni 2 secondi
  static unsigned long lastTime = 0;
  if (millis() - lastTime >= 2000) {
    int sensorValue = analogRead(SENSOR_PIN);
    float voltage = sensorValue * (3.3 / 1023.0); // HM-10 usa 3.3V
    bleSerial.print("TEMP:");
    bleSerial.println(voltage);
    lastTime = millis();
  }
}