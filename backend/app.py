# Import corretti con percorsi relativi
from .database import init_db, fetch_papers, save_experiment
from .data_fetcher import search_arxiv
from .simulation import compute_simulation
from .validation import validate_experiment
from .websocket import socketio  # Se websocket.py è separato
from .websocket import socketio
socketio.init_app(app)  # Inizializza in app.py

# Inizializza il database all'avvio
init_db()  # Chiamata diretta a database.py

# Esempio di endpoint che usa data_fetcher.py
@app.route('/search_arxiv')
def search():
    return search_arxiv("quantum physics")  # Chiamata a data_fetcher.py

# Esempio di endpoint che usa validation.py
@app.route('/validate', methods=['POST'])
def validate_data():
    data = request.json
    return validate_experiment(data)  # Chiamata a validation.py
