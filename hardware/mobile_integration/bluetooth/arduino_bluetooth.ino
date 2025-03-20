// Arduino Bluetooth Integration for iPhone and Android
#include <SoftwareSerial.h>

// Definizione dei pin per il modulo Bluetooth (TX, RX)
SoftwareSerial bluetoothSerial(10, 11); // RX | TX

// Pin per un LED di esempio
const int LED_PIN = 13;

void setup() {
  // Inizializza la comunicazione seriale con il PC
  Serial.begin(9600);
  // Inizializza la comunicazione Bluetooth
  bluetoothSerial.begin(9600);
  
  // Configura il pin del LED come output
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW); // LED spento all'avvio
  
  Serial.println("Arduino pronto per connessione Bluetooth...");
}

void loop() {
  // Controlla se ci sono dati in arrivo dal dispositivo mobile
  if (bluetoothSerial.available()) {
    char command = bluetoothSerial.read();
    
    // Comandi semplici: '1' accende il LED, '0' lo spegne
    switch (command) {
      case '1':
        digitalWrite(LED_PIN, HIGH);
        bluetoothSerial.println("LED acceso");
        Serial.println("LED acceso");
        break;
      case '0':
        digitalWrite(LED_PIN, LOW);
        bluetoothSerial.println("LED spento");
        Serial.println("LED spento");
        break;
      default:
        bluetoothSerial.println("Comando non riconosciuto");
        Serial.println("Comando non riconosciuto");
    }
  }
  
  // Invia dati di esempio al dispositivo mobile ogni 2 secondi
  static unsigned long lastSendTime = 0;
  if (millis() - lastSendTime >= 2000) {
    int sensorValue = analogRead(A0); // Legge un sensore su A0
    bluetoothSerial.print("Sensore: ");
    bluetoothSerial.println(sensorValue);
    lastSendTime = millis();
  }
}