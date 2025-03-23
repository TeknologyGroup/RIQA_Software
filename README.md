# RIQA_Software

**Sottotitolo**: Simulazione di Wormhole e Zeri della Funzione Zeta di Riemann  
**Autore**: Martino Battista  
**Data**: 20 Marzo 2025  
**Licenza**: MIT License  

---

## Panoramica

**RIQA_Software** è un framework modulare open-source progettato per esplorare la connessione teorica tra i wormhole attraversabili della relatività generale e gli zeri non banali della funzione zeta di Riemann (\( \zeta(s) \)). Il progetto integra simulazioni numeriche, visualizzazioni interattive in 2D e 3D, raccolta di dati da sensori fisici e un’interfaccia vocale, offrendo uno strumento versatile per la ricerca interdisciplinare tra fisica teorica e matematica pura.

L’ipotesi centrale propone che gli zeri non banali di \( \zeta(s) \) sulla linea critica (\( s = 1/2 + it \), es. \( t_1 \approx 14.1347 \)) possano corrispondere a singolarità o punti critici nella metrica dei wormhole, suggerendo una relazione tra la distribuzione dei numeri primi e la geometria dello spazio-tempo.

## Caratteristiche Principali

- **Simulazioni Numeriche**: Calcolo della metrica di wormhole con parametri influenzati dagli zeri di \( \zeta(s) \).
- **Visualizzazioni**: Grafici 2D interattivi (Plotly) e modelli 3D dinamici (Three.js) della geometria wormhole.
- **Integrazione Hardware**: Raccolta dati in tempo reale da sensori (es. accelerometro MPU-6050) tramite Bluetooth Low Energy (BLE).
- **Controllo Vocale**: Interfaccia assistente per avviare simulazioni con comandi vocali.
- **Database**: Archiviazione strutturata di risultati e dati sperimentali con SQLite.

## Struttura del Progetto

La struttura del repository è organizzata in modo modulare per separare chiaramente le diverse componenti:


RIQA_Software/├── frontend/                  # Interfaccia utente basata su React│   ├── src/                   # Codice sorgente del frontend│   │   ├── App.js            # Routing e layout principale dell’applicazione│   │   ├── components/       # Componenti React riutilizzabili│   │   │   ├── SimulationForm.js  # Form per avviare e configurare le simulazioni│   │   │   └── Wormhole3D.js      # Visualizzazione 3D del wormhole con Three.js│   │   └── pages/            # Pagine dell’applicazione│   │       └── Simulations.js     # Pagina dedicata alle simulazioni├── backend/                   # Server Flask per logica e API│   ├── main.py               # File principale dell’API Flask│   ├── simulations/          # Moduli per le simulazioni│   │   └── wormhole_zeta.py  # Simulazione della metrica wormhole basata su zeri zeta│   ├── assistant_interface.py # Interfaccia vocale per il controllo del software│   └── mobile_data.py        # Gestione dei dati ricevuti dai sensori via Bluetooth/BLE├── database/                 # Database SQLite per dati e risultati│   └── models/               # Modelli dei dati│       └── simulation_results.py  # Schema del database per i risultati delle simulazioni├── visualizations/           # Strumenti per la visualizzazione dei dati│   └── plots/                # Moduli per grafici│       └── wormhole_plot.py  # Grafici 2D interattivi della metrica con Plotly├── hardware/                 # Integrazione con dispositivi hardware│   └── mobile_integration/   # Comunicazione con dispositivi mobili│       ├── bluetooth/        # Script per Bluetooth e BLE│       │   └── arduino_hm10_sensors.ino  # Codice Arduino per HM-10 e sensori│       └── mobile_app/       # Applicazione mobile│           └── main.dart     # App Flutter per controllo e monitoraggio├── docs/                     # Documentazione del progetto│   ├── wormhole_zeta.md      # Teoria su wormhole e zeri della funzione zeta│   └── formulas.tex          # Raccolta di formule matematiche in LaTeX└── requirements.txt          # Elenco delle dipendenze Python


## Prerequisiti

- **Python**: 3.8 o superiore
- **Node.js**: Per il frontend React
- **Flutter**: Per l’app mobile (iOS/Android)
- **Arduino IDE**: Per caricare il codice sui dispositivi hardware
- **Hardware**: Arduino con modulo HM-10 e sensore MPU-6050 (opzionale)

## Installazione

Per avviare il progetto **RIQA_Software** su un terminale Linux (Debian) su Chromebook, segui questi passaggi passo dopo passo. Assicurati di avere già configurato l'ambiente Linux sul tuo Chromebook e di avere installato i prerequisiti necessari (Python, Node.js, Flutter, Arduino IDE, ecc.).

---

### **1. Clona il Repository**
Apri il terminale Linux e clona il repository GitHub del progetto:

```bash
git clone https://github.com/[tuo-username]/RIQA_Software.git
cd RIQA_Software
```

Sostituisci `[tuo-username]` con il tuo username GitHub o l'URL corretto del repository.

---

### **2. Installa le Dipendenze del Backend**
Installa le dipendenze Python necessarie per il backend Flask:

```bash
pip install -r requirements.txt
```

Se non hai `pip` installato, puoi installarlo con:

```bash
sudo apt update
sudo apt install python3-pip
```

---

### **3. Avvia il Backend**
Avvia il server Flask per il backend:

```bash
python backend/main.py
```

Il server Flask dovrebbe avviarsi e rimanere in esecuzione in attesa di richieste. Tieni aperto questo terminale.

---

### **4. Installa le Dipendenze del Frontend**
Apri un nuovo terminale (o una nuova scheda del terminale) e naviga nella cartella `frontend`:

```bash
cd frontend
```

Installa le dipendenze Node.js per il frontend React:

```bash
npm install
```

Installa anche la libreria `three.js` per le visualizzazioni 3D:

```bash
npm install three
```

---

### **5. Avvia il Frontend**
Avvia il server di sviluppo React:

```bash
npm start
```

Questo aprirà automaticamente il frontend nel browser predefinito all'indirizzo `http://localhost:3000`. Se non si apre automaticamente, puoi accedervi manualmente.

---

### **6. Configura l'Hardware (Opzionale)**
Se desideri utilizzare l'hardware (Arduino con modulo HM-10 e sensore MPU-6050), segui questi passaggi:

1. **Carica il Codice su Arduino**:
   - Apri il file `hardware/mobile_integration/bluetooth/arduino_hm10_sensors.ino` nell'Arduino IDE.
   - Collega l'Arduino al Chromebook e carica il codice.

2. **Avvia la Gestione dei Dati**:
   Torna al terminale principale (dove hai clonato il repository) e avvia lo script Python per la gestione dei dati:

   ```bash
   python backend/mobile_data.py
   ```

---

### **7. Configura l'App Mobile (Opzionale)**
Se desideri utilizzare l'app mobile Flutter:

1. Installa Flutter sul Chromebook (se non lo hai già fatto):
   - Segui la guida ufficiale: https://flutter.dev/docs/get-started/install/linux

2. Naviga nella cartella dell'app mobile:

   ```bash
   cd hardware/mobile_integration/mobile_app/
   ```

3. Installa le dipendenze Flutter:

   ```bash
   flutter pub get
   ```

4. Avvia l'app:

   ```bash
   flutter run
   ```

---

### **8. Utilizzo del Software**
Ora che tutto è configurato, puoi utilizzare il software:

1. **Frontend**:
   - Apri `http://localhost:3000` nel browser.
   - Vai alla pagina "Simulations" e inserisci un indice dello zero non banale (es. "1" per \( t_1 \approx 14.1347 \)) nel form.
   - Clicca "Esegui Simulazione" per avviare la simulazione.

2. **Visualizzazione**:
   - I grafici 2D della metrica verranno visualizzati con Plotly.
   - Il modello 3D interattivo del wormhole verrà visualizzato con Three.js.

3. **Dati Hardware**:
   - Se hai configurato l'hardware, i dati dei sensori verranno raccolti e correlati con i parametri della simulazione.

---

### **9. Debug e Risoluzione dei Problemi**
- Se incontri errori, verifica che tutte le dipendenze siano installate correttamente.
- Controlla che i server Flask e React siano in esecuzione.
- Se utilizzi l'hardware, assicurati che l'Arduino sia correttamente collegato e configurato.

---

### **10. Fermare i Servizi**
Per fermare i servizi:
- Premi `Ctrl + C` nei terminali dove sono in esecuzione Flask (`backend/main.py`) e React (`npm start`).

---

Seguendo questi passaggi, dovresti essere in grado di avviare e utilizzare il progetto **RIQA_Software** sul tuo Chromebook con Linux Debian.

