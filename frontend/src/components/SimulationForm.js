import React, { useState } from 'react';

function SimulationForm() {
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) {
      setError('Inserisci parametri validi');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:5000/simulate/wormhole', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ zero_index: parseInt(input), r_range: 10, points: 100 }),
      });
      if (!response.ok) throw new Error('Errore nella simulazione');
      const result = await response.json();
      console.log('Risultato:', result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const startVoiceAssistant = () => {
    fetch('http://localhost:5000/assistant/start', { method: 'POST' })
      .then(() => console.log('Assistente vocale avviato'))
      .catch(err => setError('Errore assistente: ' + err.message));
  };

  return (
    <form onSubmit={handleSubmit} className="simulation-form">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Indice zero (es. 1)"
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'In esecuzione...' : 'Esegui Simulazione'}
      </button>
      <button type="button" onClick={startVoiceAssistant} disabled={loading}>
        Assistente Vocale
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

export default SimulationForm;