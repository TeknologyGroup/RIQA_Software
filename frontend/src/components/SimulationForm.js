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
      const response = await fetch('http://localhost:5000/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ parameters: input }),
      });

      if (!response.ok) throw new Error('Errore nella simulazione');
      const result = await response.json();
      console.log('Risultato simulazione:', result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="simulation-form">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Inserisci i parametri (es. mu=0.1, N=100)"
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'In esecuzione...' : 'Esegui Simulazione'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

export default SimulationForm;