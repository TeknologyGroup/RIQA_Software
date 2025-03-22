#include <SoftwareSerial.h>
#include <DHT.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>

#define DHTPIN 2
#define DHTTYPE DHT22
#define LED_PIN 13

SoftwareSerial bluetoothSerial(10, 11); // RX | TX
DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP280 bmp;

void setup() {
    Serial.begin(9600);
    bluetoothSerial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    dht.begin();
    if (!bmp.begin(0x76)) {
        Serial.println("Errore BMP280");
        bluetoothSerial.println("Errore BMP280");
    }
}

void loop() {
    // Leggi dati sensori
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();
    float pressure = bmp.readPressure() / 100.0F; // Converti in hPa

    // Invia dati via Bluetooth
    bluetoothSerial.print("TEMP:");
    bluetoothSerial.println(temperature);
    bluetoothSerial.print("HUMID:");
    bluetoothSerial.println(humidity);
    bluetoothSerial.print("PRESS:");
    bluetoothSerial.println(pressure);

    // Controllo LED
    if (bluetoothSerial.available()) {
        char command = bluetoothSerial.read();
        if (command == '1') {
            digitalWrite(LED_PIN, HIGH);
            bluetoothSerial.println("LED acceso");
        } else if (command == '0') {
            digitalWrite(LED_PIN, LOW);
            bluetoothSerial.println("LED spento");
        }
    }

    delay(2000); // Ritardo per evitare sovraccarico
}

### **1.2. Calibrazione Automatica** ###

#Implementa una calibrazione automatica per i sensori, se necessario.#

void calibrateSensors() {
    // Calibrazione BMP280 (esempio)
    float baselinePressure = bmp.readPressure() / 100.0F;
    bluetoothSerial.print("Pressione di base: ");
    bluetoothSerial.println(baselinePressure);
}
