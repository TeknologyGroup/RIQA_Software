# Installazione di RIQA_Software

## Prerequisiti

- **Python**: 3.8 o superiore
- **Node.js**: Per il frontend React
- **Flutter**: Per l’app mobile (opzionale)
- **Arduino IDE**: Per caricare il codice sui dispositivi hardware (opzionale)

## Installazione del Backend

1. Clona il repository:
   ```bash
   git clone https://github.com/TeknologyGroup/RIQA_Software.git
   cd RIQA_Software

1. Installa le dipendenze Python:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
2. Avvia il server Flask:
    
    ```bash
    python backend/main.py
    
    ```
    

## Installazione del Frontend

1. Vai alla directory del frontend:
    
    ```bash
    cd frontend
    
    ```
    
2. Installa le dipendenze Node.js:
    
    ```bash
    npm install
    
    ```
    
3. Avvia il server di sviluppo:
    
    ```bash
    npm start
    
    ```
    

## Installazione dell'App Mobile (opzionale)

1. Installa Flutter e apri la directory dell'app mobile:
    
    ```bash
    cd hardware/mobile_integration/mobile_app
    
    ```
    
2. Avvia l'app:
    
    ```bash
    flutter run
    
    ```
    

```

##### **1.2.3. Guida Introduttiva**
```markdown
# Guida Introduttiva

## Avvio di una Simulazione

1. Apri il frontend all'indirizzo `http://localhost:3000`.
2. Vai alla pagina "Simulations".
3. Inserisci i parametri della simulazione (es. indice dello zero non banale).
4. Clicca su "Esegui Simulazione".

## Visualizzazione dei Risultati

- **Grafici 2D**: I risultati delle simulazioni sono visualizzati in grafici interattivi.
- **Modelli 3D**: Esplora la geometria del wormhole in 3D.

```
