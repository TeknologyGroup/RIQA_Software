import React from 'react';

function Home() {
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Benvenuto in RIQA_Software</h1>
      <p>Simulazione di Wormhole e Zeri della Funzione Zeta di Riemann</p>

      <h2>Panoramica del Progetto</h2>
      <p>
        RIQA_Software è un framework modulare open-source progettato per esplorare la connessione teorica tra i wormhole attraversabili della relatività generale e gli zeri non banali della funzione zeta di Riemann.
      </p>

      <h2>Caratteristiche Principali</h2>
      <ul style={{ textAlign: 'left', margin: '0 auto', maxWidth: '600px' }}>
        <li><strong>Simulazioni Numeriche</strong>: Calcolo della metrica di wormhole con parametri influenzati dagli zeri di ζ(s).</li>
        <li><strong>Visualizzazioni</strong>: Grafici 2D interattivi (Plotly) e modelli 3D dinamici (Three.js) della geometria wormhole.</li>
        <li><strong>Integrazione Hardware</strong>: Raccolta dati in tempo reale da sensori (es. accelerometro MPU-6050) tramite Bluetooth Low Energy (BLE).</li>
        <li><strong>Controllo Vocale</strong>: Interfaccia assistente per avviare simulazioni con comandi vocali.</li>
        <li><strong>Database</strong>: Archiviazione strutturata di risultati e dati sperimentali con SQLite.</li>
      </ul>

      <h2>Struttura del Progetto</h2>
      <p>
        Il progetto è organizzato in modo modulare, con una chiara separazione tra frontend, backend, database e integrazione hardware. Per ulteriori dettagli, consulta la documentazione.
      </p>

      <h2>Come Contribuire</h2>
      <p>
        Se sei interessato a contribuire al progetto, visita il repository GitHub e segui le istruzioni per aprire una pull request o segnalare un problema.
      </p>
    </div>
  );
}

export default Home;
