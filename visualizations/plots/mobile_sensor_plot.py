import plotly.graph_objects as go
from database.models.simulation_results import SimulationResult
from sqlalchemy.orm import Session
from database.base import engine

def create_mobile_sensor_plot():
    """Crea un grafico interattivo dei dati ricevuti dai dispositivi mobili."""
    with Session(engine) as session:
        results = session.query(SimulationResult).filter_by(simulation_type="mobile_sensor").all()
        
        if not results:
            return go.Figure()  # Grafico vuoto se non ci sono dati
        
        times = list(range(len(results)))
        values = [float(r.results.split(": ")[1]) if ": " in r.results else 0 for r in results]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Dati Sensore Mobile',
            line=dict(color='green', width=2)
        ))
        
        fig.update_layout(
            title="Dati Sensore da Dispositivi Mobili",
            xaxis_title="Tempo (indice)",
            yaxis_title="Valore Sensore",
            template="plotly_white",
            responsive=True
        )
       # Aggiungi pulsanti per esportare in PNG, PDF e SVG

import plotly.graph_objects as go
import plotly.io as pio
from database.models.simulation_results import SimulationResult
from sqlalchemy.orm import Session
from database.base import engine

def create_mobile_sensor_plot():
    """Crea un grafico interattivo dei dati ricevuti dai dispositivi mobili."""
    with Session(engine) as session:
        results = session.query(SimulationResult).filter_by(simulation_type="mobile_sensor").all()

        if not results:
            return go.Figure()  # Grafico vuoto se non ci sono dati

        times = list(range(len(results)))
        values = [float(r.results.split(": ")[1]) if ": " in r.results else 0 for r in results]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Dati Sensore Mobile',
            line=dict(color='green', width=2)
        ))

        fig.update_layout(
            title="Dati Sensore da Dispositivi Mobili",
            xaxis_title="Tempo (indice)",
            yaxis_title="Valore Sensore",
            template="plotly_white",
            responsive=True
        )

        # Aggiungi pulsanti per esportare in PNG, PDF e SVG
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                buttons=[
                    dict(label="Esporta PNG",
                         method="download_image",
                         args=["mobile_sensor_plot.png", "png"]),
                    dict(label="Esporta PDF",
                         method="download_image",
                         args=["mobile_sensor_plot.pdf", "pdf"]),
                    dict(label="Esporta SVG",
                         method="download_image",
                         args=["mobile_sensor_plot.svg", "svg"])
                ],
                direction="left",
                showactive=False,
                x=1.0,
                y=1.1
            )]
        )

        return fig

def export_plot(fig: go.Figure, filename: str, format: str = 'png'):
    """
    Esporta un grafico Plotly come immagine.

    Args:
        fig: Oggetto Figure di Plotly.
        filename: Nome del file di output.
        format: Formato dell'immagine (es. 'png', 'pdf', 'svg').
    """
    pio.write_image(fig, filename, format=format)


### **2.2. Personalizzazione Avanzata** ###

#Aggiungi più opzioni di personalizzazione, come la scelta di colori, stili e temi.


def create_mobile_sensor_plot(theme: str = 'plotly_white', line_color: str = 'green'):
    """Crea un grafico interattivo dei dati ricevuti dai dispositivi mobili."""
    with Session(engine) as session:
        results = session.query(SimulationResult).filter_by(simulation_type="mobile_sensor").all()

        if not results:
            return go.Figure()  # Grafico vuoto se non ci sono dati

        times = list(range(len(results)))
        values = [float(r.results.split(": ")[1]) if ": " in r.results else 0 for r in results]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Dati Sensore Mobile',
            line=dict(color=line_color, width=2)
        ))

        fig.update_layout(
            title="Dati Sensore da Dispositivi Mobili",
            xaxis_title="Tempo (indice)",
            yaxis_title="Valore Sensore",
            template=theme,
            responsive=True
        )

        # Aggiungi pulsanti per esportare in PNG, PDF e SVG
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                buttons=[
                    dict(label="Esporta PNG",
                         method="download_image",
                         args=["mobile_sensor_plot.png", "png"]),
                    dict(label="Esporta PDF",
                         method="download_image",
                         args=["mobile_sensor_plot.pdf", "pdf"]),
                    dict(label="Esporta SVG",
                         method="download_image",
                         args=["mobile_sensor_plot.svg", "svg"])
                ],
                direction="left",
                showactive=False,
                x=1.0,
                y=1.1
            )]
        )

        return fig

        
