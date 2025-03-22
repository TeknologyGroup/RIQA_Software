import plotly.graph_objects as go

def create_evolution_plot(time: list, frequency: list) -> go.Figure:
    """
    Crea un grafico interattivo dell'evoluzione allelica.
    
    Args:
        time: Lista dei tempi.
        frequency: Lista delle frequenze alleliche.
    
    Returns:
        Oggetto Figure di Plotly.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time, 
        y=frequency, 
        mode='lines', 
        name='Frequenza Allelica',
        line=dict(color='royalblue', width=2)
    ))
    
    fig.update_layout(
        title="Simulazione Evolutiva",
        xaxis_title="Tempo",
        yaxis_title="Frequenza Allelica",
        template="plotly_white",
        responsive=True,
        margin=dict(l=50, r=50, t=50, b=50),
        hovermode="x unified"
    )
    
    # Aggiunge pulsante per esportare come PNG
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Esporta PNG",
                         method="relayout",
                         args=["images", {"format": "png"}])],
            direction="left",
            showactive=False,
            x=1.0,
            y=1.1
        )]
    )
    
    return fig
    
    # visualizations/plots/evolution_plot.py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_evolution_plot(time: list, frequency: list, theme: str = 'plotly_white') -> go.Figure:
    """
    Crea un grafico interattivo dell'evoluzione allelica con personalizzazione avanzata.

    Args:
        time: Lista dei tempi.
        frequency: Lista delle frequenze alleliche.
        theme: Tema del grafico (es. 'plotly', 'plotly_white', 'plotly_dark').

    Returns:
        Oggetto Figure di Plotly.
    """
    fig = go.Figure()

    # Aggiungi traccia principale
    fig.add_trace(go.Scatter(
        x=time,
        y=frequency,
        mode='lines',
        name='Frequenza Allelica',
        line=dict(color='royalblue', width=2, dash='solid'),
        hoverlabel=dict(bgcolor='white', font_size=12)
    ))

    # Personalizza il layout
    fig.update_layout(
        title="Simulazione Evolutiva",
        xaxis_title="Tempo",
        yaxis_title="Frequenza Allelica",
        template=theme,
        hovermode="x unified",
        margin=dict(l=50, r=50, t=50, b=50),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255, 255, 255, 0.5)'),
        font=dict(family="Arial, sans-serif", size=12, color="black")
    )

    # Aggiungi pulsante per esportare come PNG
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Esporta PNG",
                         method="relayout",
                         args=["images", {"format": "png"}])],
            direction="left",
            showactive=False,
            x=1.0,
            y=1.1
        )]
    )

    return fig