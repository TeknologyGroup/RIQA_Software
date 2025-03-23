# Architettura di RIQA_Software

## Componenti Principali

- **Frontend**: Interfaccia utente basata su React.
- **Backend**: Server Flask per la gestione delle simulazioni e delle API.
- **Database**: SQLite per l'archiviazione dei dati.
- **Visualizzazioni**: Grafici interattivi con Plotly e modelli 3D con Three.js.
- **Integrazione Hardware**: Comunicazione con dispositivi Arduino tramite Bluetooth/BLE.

## Diagramma dell'Architettura

![Diagramma Architettura](architecture_diagram.png)

docs/
├── developer_guide/
│   ├── architecture.md         # Architettura del software
│   ├── technologies.md        # Tecnologie utilizzate
│   ├── setup_development.md   # Configurazione dell'ambiente di sviluppo
│   ├── contributing.md        # Linee guida per contribuire
│   ├── api_reference.md       # Documentazione delle API
│   ├── testing.md             # Test automatici
│   └── deployment.md          # Distribuzione del software
