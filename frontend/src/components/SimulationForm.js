import React, { useState } from 'react';

function SimulationForm(props) {
  const [input, setInput] = useState(''); // Indice dello zero non banale
  const [loading, setLoading] = useState(false); // Stato di caricamento
  const [error, setError] = useState(null); // Messaggi di errore

  // Gestisce l'invio del form per avviare la simulazione
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || isNaN(input)) {
      setError('Inserisci un indice valido (es. 1)');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const zeroIndex = parseInt(input);
      const response = await fetch('http://localhost:5000/simulate/wormhole', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          zero_index: zeroIndex,
          r_range: 10, // Intervallo radiale fisso per semplicità
          points: 100, // Numero di punti per la simulazione
        }),
      });

      if (!response.ok) {
        throw new Error('Errore nella simulazione: ' + response.statusText);
      }

      const result = await response.json();
      console.log('Risultato simulazione:', result);

      // Passa i dati al componente genitore (es. per visualizzazione 3D)
      if (props.onResult) {
        props.onResult(result);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Avvia l'assistente vocale tramite una richiesta al backend
  const startVoiceAssistant = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/assistant/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        throw new Error('Errore nell’avvio dell’assistente');
      }
      console.log('Assistente vocale avviato');
    } catch (err) {
      setError('Errore assistente: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="simulation-form-container">
      <form onSubmit={handleSubmit} className="simulation-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Indice zero (es. 1)"
          disabled={loading}
          style={{ padding: '8px', marginRight: '10px', width: '150px' }}
        />
        <button
          type="submit"
          disabled={loading}
          style={{ padding: '8px 16px', backgroundColor: '#4CAF50', color: 'white', border: 'none' }}
        >
          {loading ? 'In esecuzione...' : 'Esegui Simulazione'}
        </button>
        <button
          type="button"
          onClick={startVoiceAssistant}
          disabled={loading}
          style={{ padding: '8px 16px', backgroundColor: '#2196F3', color: 'white', border: 'none', marginLeft: '10px' }}
        >
          {loading ? 'Avvio...' : 'Assistente Vocale'}
        </button>
      </form>
      {error && (
        <p style={{ color: 'red', marginTop: '10px' }}>{error}</p>
      )}
      <style jsx>{`
        .simulation-form-container {
          padding: 20px;
          text-align: center;
        }
        .simulation-form {
          display: inline-flex;
          align-items: center;
        }
        button:hover:not(:disabled) {
          opacity: 0.9;
          cursor: pointer;
        }
        button:disabled {
          background-color: #cccccc;
        }
      `}</style>
    </div>
  );
}

export default SimulationForm;