###Integra più sensori, come un sensore di luce (LDR) e un sensore di gas (MQ-2), oltre al controllo del LED.###

#include <SoftwareSerial.h>

#define LED_PIN 13
#define LDR_PIN A0
#define MQ2_PIN A1

SoftwareSerial bleSerial(10, 11); // RX | TX

void setup() {
    Serial.begin(9600);
    bleSerial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
}

void loop() {
    // Leggi dati sensori
    int ldrValue = analogRead(LDR_PIN);
    int mq2Value = analogRead(MQ2_PIN);

    // Invia dati via BLE
    bleSerial.print("LDR:");
    bleSerial.println(ldrValue);
    bleSerial.print("MQ2:");
    bleSerial.println(mq2Value);

    // Controllo LED
    if (bleSerial.available()) {
        char command = bleSerial.read();
        if (command == '1') {
            digitalWrite(LED_PIN, HIGH);
            bleSerial.println("LED acceso");
        } else if (command == '0') {
            digitalWrite(LED_PIN, LOW);
            bleSerial.println("LED spento");
        }
    }

    delay(2000); // Ritardo per evitare sovraccarico
}

### **2.2. Gestione Avanzata degli Errori**###

#Aggiungi un sistema di gestione degli errori per la connessione BLE.#

void checkBLEConnection() {
    if (!bleSerial.available()) {
        Serial.println("Errore connessione BLE");
        bleSerial.println("Errore connessione BLE");
    }
}

void loop() {
    checkBLEConnection();
    // Leggi e invia dati sensori
    // ...
}
