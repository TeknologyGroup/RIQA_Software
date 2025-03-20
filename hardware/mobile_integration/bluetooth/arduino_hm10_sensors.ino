#include <SoftwareSerial.h>
#include <Wire.h>
#include <MPU6050.h>

SoftwareSerial bleSerial(10, 11); // RX | TX
MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  bleSerial.begin(9600);
  Wire.begin();
  mpu.initialize();
  
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
  
  // Calcola accelerazione totale (in m/s^2)
  float accel = sqrt(ax*ax + ay*ay + az*az) / 16384.0 * 9.81;
  
  // Invia via BLE
  bleSerial.print("ACCEL:");
  bleSerial.println(accel);
  Serial.print("Accelerazione: ");
  Serial.println(accel);
  
  // Ritardo
  delay(1000);
}