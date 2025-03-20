# Integrazione Mobile con Arduino

Questo file descrive come configurare un'app mobile per comunicare con Arduino tramite Bluetooth.

## Requisiti
- **Modulo Bluetooth**: HC-05 o HC-06 collegato ad Arduino.
- **App Mobile**:
  - **Android**: Usa "Bluetooth Serial Terminal" (disponibile su Play Store) o sviluppa un'app con Android Studio.
  - **iPhone**: Usa "BLE Scanner" o "nRF Connect" (App Store) per connettersi al modulo Bluetooth.

## Passaggi per la Configurazione

### Android
1. **Accoppiamento**:
   - Vai su Impostazioni > Bluetooth.
   - Cerca il dispositivo HC-05/HC-06 e accoppialo (PIN default: "1234" o "0000").
2. **App Bluetooth Serial Terminal**:
   - Apri l'app e connettiti al dispositivo HC-05/HC-06.
   - Imposta la baud rate a 9600.
   - Invia '1' per accendere il LED, '0' per spegnerlo.
   - Visualizza i dati del sensore ricevuti.

### iPhone
1. **Connessione**:
   - Apri "nRF Connect" o "BLE Scanner".
   - Cerca il modulo Bluetooth e connettiti.
   - Usa il servizio UART (se configurato sul modulo) per inviare/ricevere dati.
2. **Comandi**:
   - Invia '1' o '0' come stringhe per controllare il LED.
   - Leggi i dati del sensore in arrivo.

## Sviluppo Personalizzato
- **Android**: Usa la libreria Bluetooth di Android (BluetoothSocket) per creare un'app personalizzata.
- **iOS**: Usa CoreBluetooth per sviluppare un'app in Swift che si connetta al modulo.

## Note
- Assicurati che il modulo Bluetooth sia configurato come "slave" (default per HC-05).
- Per una comunicazione bidirezionale avanzata, considera l'uso di un modulo BLE (es. HM-10).