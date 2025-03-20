# RIQA_Software

**Sottotitolo**: Wormhole e Zeri della Funzione Zeta  
**Autore**: Martino Battista  
**Data**: 20 Marzo 2025

---

## Descrizione
RIQA_Software è un framework modulare per simulare wormhole attraversabili e indagare la loro possibile connessione con gli zeri non banali della funzione zeta di Riemann (\( \zeta(s) \)). Integra simulazioni numeriche, visualizzazioni 2D/3D, raccolta dati da sensori e controllo vocale.

L’ipotesi centrale è che gli zeri non banali (\( s = 1/2 + it \), es. \( t_1 \approx 14.1347 \)) corrispondano a singolarità o punti critici nella metrica dei wormhole, suggerendo un legame tra matematica pura e viaggi spazio-temporali.

## Struttura del Progetto

RIQA_Software/├── frontend/                  # Interfaccia React│   ├── src/│   │   ├── App.js            # Routing e layout│   │   ├── components/│   │   │   ├── SimulationForm.js  # Form per simulazioni│   │   │   └── Wormhole3D.js      # Visualizzazione 3D con Three.js│   │   └── pages/│   │       └── Simulations.js     # Pagina simulazioni├── backend/                   # Server Flask│   ├── main.py               # API principale│   ├── simulations/│   │   └── wormhole_zeta.py  # Simulazione wormhole-zeta│   ├── assistant_interface.py # Assistente vocale│   └── mobile_data.py        # Gestione dati sensori├── database/                 # SQLite│   └── models/│       └── simulation_results.py  # Modello database├── visualizations/           # Grafici│   └── plots/│       └── wormhole_plot.py  # Grafici 2D con Plotly├── hardware/                 # Integrazione hardware│   └── mobile_integration/│       ├── bluetooth/│       │   ├── arduino_hm10_sensors.ino  # Arduino con HM-10│       └── mobile_app/│           └── main.dart     # App Flutter├── docs/                     # Documentazione│   ├── wormhole_zeta.md      # Teoria│   └── formulas.tex          # Formule matematiche└── requirements.txt          # Dipendenze Python


## Funzionalità Principali
- **Simulazioni**: Calcola metriche wormhole (es. \( ds^2 \)) con \( b_0 = t_n \).
- **Visualizzazioni**: Grafici 2D (Plotly) e 3D (Three.js) della gola e curvatura.
- **Hardware**: Raccolta dati accelerometrici via BLE (HM-10 + MPU-6050).
- **Assistente Vocale**: Controllo tramite comandi (es. "simula wormhole con zero 2").
- **Teoria**: Ipotesi \( \zeta(s) = \int_{\partial M} O(x)^s \, d\mu(x) \).

## Installazione

### Prerequisiti
- Python 3.8+
- Node.js (per frontend)
- Flutter (per app mobile)
- Arduino IDE (per hardware)

### Setup
1. **Clona il repository**:
   ```bash
   git clone https://github.com/tuo-username/RIQA_Software.git
   cd RIQA_Software

	1.	Backend:
pip install -r requirements.txt
python backend/main.py

	2.	Frontend:
cd frontend
npm install
npm install three
npm start

	3.	Hardware:
	•	Carica arduino_hm10_sensors.ino su Arduino con HM-10 e MPU-6050.
	•	Esegui backend/mobile_data.py.
	4.	App Mobile:
	•	Configura Flutter e avvia main.dart.

Uso

	•	Simulazione: Inserisci un indice zero nel form o usa l’assistente vocale.
	•	Visualizzazione: Visualizza la metrica in 2D o 3D.
	•	Dati Sensori: Correlali con ( b_0 ) via mobile_data.py.

Teoria

La metrica del wormhole è:[ds^2 = -e^{2\Phi(r)} dt^2 + \frac{dr^2}{1 - \frac{b(r)}{r}} + r^2 (d\theta^2 + \sin^2\theta , d\phi^2),]con ( b_0 = t_n ) derivato dagli zeri di ( \zeta(s) ). L’integrale proposto è:[\zeta(s) \approx 4^s b_0^{2-2s} \cdot 4\pi.]

Contributi

Pull request e suggerimenti sono benvenuti! Contatta [tuo-email] per collaborazioni.

Licenza

MIT License
