# app/__init__.py
"""
Modulo di inizializzazione dell'applicazione Flask per RIQA_Software.
Configura l'app con gestione errori, logging strutturato, metriche Prometheus,
documentazione Swagger e logging per SQLAlchemy.
"""

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import logging
import structlog
from structlog import configure, get_logger
from prometheus_flask_exporter import PrometheusMetrics
from flasgger import Swagger
from sqlalchemy import event
from sqlalchemy.engine import Engine


def create_app():
    """
    Crea e configura un'istanza dell'applicazione Flask con tutte le funzionalità richieste.
    
    Returns:
        Flask: L'applicazione Flask configurata.
    """
    # Inizializza l'app Flask
    app = Flask(__name__)

    # --- Gestione degli Errori ---
    @app.errorhandler(Exception)
    def handle_exception(e):
        """
        Gestisce tutte le eccezioni nell'app Flask, restituendo risposte JSON standardizzate.
        
        Args:
            e (Exception): L'eccezione sollevata.
        
        Returns:
            Response: Risposta JSON con codice di stato appropriato.
        """
        if isinstance(e, HTTPException):
            # Gestisce errori HTTP specifici (es. 404, 400)
            response = jsonify({
                'error': e.name,           # Nome dell'errore (es. "Not Found")
                'message': e.description   # Descrizione dell'errore
            })
            response.status_code = e.code
        else:
            # Gestisce errori generici (500 Internal Server Error)
            response = jsonify({
                'error': 'Internal Server Error',
                'message': str(e)          # Dettaglio dell'errore non previsto
            })
            response.status_code = 500
        return response

    # --- Configurazione del Logging Strutturato ---
    configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),  # Aggiunge timestamp ISO
            structlog.processors.JSONRenderer()           # Output in formato JSON
        ],
        context_class=dict,                              # Usa dizionario per contesto
        logger_factory=structlog.stdlib.LoggerFactory()  # Integra con logging stdlib
    )
    # Sostituisci il logger di Flask con uno strutturato
    app.logger = get_logger(__name__)
    app.logger.info("Applicazione Flask inizializzata")

    # --- Metriche Prometheus ---
    metrics = PrometheusMetrics(app)  # Integra Prometheus per monitorare le richieste
    # Configura metriche di default (es. latenza, conteggio richieste)
    metrics.info('app_info', 'Informazioni sull’app RIQA_Software', version='1.0.0')

    # --- Documentazione Swagger ---
    swagger_config = {
        "title": "RIQA_Software API",
        "uiversion": 3,
        "description": "API per simulazioni wormhole e Quantum Chaos Fingerprinting"
    }
    Swagger(app, config=swagger_config)  # Avvia Swagger per documentazione API interattiva

    # --- Logging per SQLAlchemy ---
    # Configura il logging di base
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    @event.listens_for(Engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        """
        Registra ogni query SQLAlchemy prima dell’esecuzione per debugging e monitoraggio.
        
        Args:
            conn: Connessione al database.
            cursor: Cursore SQL.
            statement: Query SQL da eseguire.
            parameters: Parametri della query.
            context: Contesto di esecuzione.
            executemany: Flag per esecuzione multipla.
        """
        app.logger.info(
            "Esecuzione query SQL",
            statement=statement,
            parameters=parameters,
            executemany=executemany
        )

    # Restituisci l’app configurata
    return app


# Punto di ingresso per test standalone (opzionale)
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)