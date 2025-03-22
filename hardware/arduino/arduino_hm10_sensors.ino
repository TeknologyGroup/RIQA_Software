#supporto per più sensori, come sensori di temperatura, umidità, pressione, ecc.#

#include <SoftwareSerial.h>
#include <Wire.h>
#include <MPU6050.h>
#include <DHT.h>

SoftwareSerial bleSerial(10, 11); // RX | TX
MPU6050 mpu;
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    bleSerial.begin(9600);
    Wire.begin();
    mpu.initialize();
    dht.begin();

    if (mpu.testConnection()) {
        Serial.println("MPU6050 connesso");
        bleSerial.println("MPU6050 connesso");
    } else {
        Serial.println("Errore MPU6050");
        bleSerial.println("Errore MPU6050");
    }
}

void loop() {
    // Leggi dati accelerometro
    int16_t ax, ay, az;
    mpu.getAcceleration(&ax, &ay, &az);
    float accel = sqrt(ax*ax + ay*ay + az*az) / 16384.0 * 9.81;

    // Leggi dati temperatura e umidità
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Invia dati via BLE
    bleSerial.print("ACCEL:");
    bleSerial.println(accel);
    bleSerial.print("TEMP:");
    bleSerial.println(temperature);
    bleSerial.print("HUMID:");
    bleSerial.println(humidity);

    // Ritardo
    delay(1000);
}

# gestione modulare per i sensori, in modo da poter aggiungere o rimuovere sensori facilmente#

void readAndSendSensorData() {
    // Leggi e invia dati da tutti i sensori
    readAndSendAccelerometerData();
    readAndSendTemperatureData();
    readAndSendHumidityData();
}

void readAndSendAccelerometerData() {
    int16_t ax, ay, az;
    mpu.getAcceleration(&ax, &ay, &az);
    float accel = sqrt(ax*ax + ay*ay + az*az) / 16384.0 * 9.81;
    bleSerial.print("ACCEL:");
    bleSerial.println(accel);
}

void readAndSendTemperatureData() {
    float temperature = dht.readTemperature();
    bleSerial.print("TEMP:");
    bleSerial.println(temperature);
}

void readAndSendHumidityData() {
    float humidity = dht.readHumidity();
    bleSerial.print("HUMID:");
    bleSerial.println(humidity);
}

void loop() {
    readAndSendSensorData();
    delay(1000);
}

# gestione robusta degli errori di comunicazione, inclusi timeout e riconnessioni automatiche#

void setup() {
    Serial.begin(9600);
    bleSerial.begin(9600);
    Wire.begin();
    mpu.initialize();
    dht.begin();

    if (!mpu.testConnection()) {
        Serial.println("Errore MPU6050");
        bleSerial.println("Errore MPU6050");
    }
}

void loop() {
    if (bleSerial.available()) {
        String command = bleSerial.readString();
        if (command == "RECONNECT") {
            bleSerial.begin(9600);
            bleSerial.println("Riconnessione avvenuta");
        }
    }

    readAndSendSensorData();
    delay(1000);
}
# sistema di logging per tracciare gli errori e facilitare il debug#

void logError(const String& errorMessage) {
    Serial.println("ERRORE: " + errorMessage);
    bleSerial.println("ERRORE: " + errorMessage);
}

void setup() {
    Serial.begin(9600);
    bleSerial.begin(9600);
    Wire.begin();
    mpu.initialize();
    dht.begin();

    if (!mpu.testConnection()) {
        logError("MPU6050 non connesso");
    }
}

#protocollo di comunicazione strutturato per inviare e ricevere dati in modo efficiente#

void sendData(const String& sensorType, float value) {
    String data = sensorType + ":" + String(value);
    bleSerial.println(data);
}

void loop() {
    readAndSendSensorData();
    delay(1000);
}

# Implementa la compressione dei dati per ridurre il traffico sulla connessione BLE.#

void sendCompressedData(const String& sensorType, float value) {
    String data = sensorType + ":" + String(value, 2); // Limita a 2 decimali
    bleSerial.println(data);
}

