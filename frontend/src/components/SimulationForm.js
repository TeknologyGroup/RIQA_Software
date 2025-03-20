const handleSubmit = async (e) => {
  // ... (codice esistente)
  const result = await response.json();
  console.log('Risultato:', result);
  if (props.onResult) props.onResult(result); // Passa i dati al genitore
  // ... (codice esistente)
};