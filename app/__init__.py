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
