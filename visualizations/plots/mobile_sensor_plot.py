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
        
        return fig