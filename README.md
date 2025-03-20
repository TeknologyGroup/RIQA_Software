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

1. **Clona il Repository**:
   ```bash
   git clone https://github.com/[tuo-username]/RIQA_Software.git
   cd RIQA_Software

	1.	Installa il Backend:
pip install -r requirements.txt
python backend/main.py

	2.	Installa il Frontend:
cd frontend
npm install
npm install three
npm start

	3.	Configura l’Hardware (opzionale):
	•	Carica hardware/mobile_integration/bluetooth/arduino_hm10_sensors.ino su un Arduino con HM-10 e MPU-6050.
	•	Esegui:
python backend/mobile_data.py

	4.	Configura l’App Mobile (opzionale):
	•	Installa Flutter e apri hardware/mobile_integration/mobile_app/.
	•	Esegui:
flutter run


Utilizzo

	1.	Avvia una Simulazione:
	•	Apri il frontend (http://localhost:3000), vai alla pagina “Simulations”.
	•	Inserisci un indice dello zero non banale (es. “1” per ( t_1 \approx 14.1347 )) nel form e clicca “Esegui Simulazione”.
	•	Oppure usa l’assistente vocale con “Simula wormhole con zero [numero]”.
	2.	Visualizza i Risultati:
	•	Grafici 2D della metrica (es. ( b(r) ), ( \Phi(r) )) con Plotly.
	•	Modello 3D interattivo della gola del wormhole con Three.js.
	3.	Raccogli Dati dai Sensori:
	•	Connetti l’Arduino e avvia mobile_data.py per correlare dati fisici (es. accelerazione) con ( b_0 ).

Fondamenti Teorici

La metrica di un wormhole attraversabile è definita come:[ds^2 = -e^{2\Phi(r)} dt^2 + \frac{dr^2}{1 - \frac{b(r)}{r}} + r^2 (d\theta^2 + \sin^2\theta , d\phi^2),]dove ( b_0 = t_n ) (es. ( t_1 \approx 14.1347 )) è derivato dagli zeri non banali di ( \zeta(s) ).

L’ipotesi propone:[\zeta(s) = \int_{\partial M} O(x)^s , d\mu(x),]con ( O(x) ) come curvatura scalare ( R \approx \frac{4 b_0}{r^3} ), suggerendo che gli zeri stabilizzano la geometria.

Per dettagli, consulta docs/wormhole_zeta.md e docs/formulas.tex.

Applicazioni

	•	Ricerca: Esplorazione di connessioni tra ( \zeta(s) ) e relatività generale.
	•	Educazione: Strumento per insegnare fisica teorica e matematica avanzata.
	•	Prototipazione: Test di correlazioni fisiche con dati sperimentali.

Contributi

Contributi sono benvenuti! Apri una pull request o segnala un problema (issue) su GitHub. Per collaborazioni, contatta genesis-quantum@proton.me martinobattista@gmail.com

Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file LICENSE per dettagli.