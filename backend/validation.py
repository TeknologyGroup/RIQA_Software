from .database import fetch_papers  # Se necessario

def validate_experiment(data):
    # Esempio: recupera dati dal DB e valida
    papers = fetch_papers()  # Chiamata a database.py
    return {"status": "success", "data": data}
