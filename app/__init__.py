# app/__init__.py
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

def create_app():
    app = Flask(__name__)

    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            response = jsonify({
                'error': e.name,
                'message': e.description
            })
            response.status_code = e.code
        else:
            response = jsonify({
                'error': 'Internal Server Error',
                'message': str(e)
            })
            response.status_code = 500
        return response

    return app



import logging
from structlog import configure, get_logger

def create_app():
    app = Flask(__name__)

    # Configurazione del logging
    configure(
        processors=[
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
    )
    app.logger = get_logger()

    return app
