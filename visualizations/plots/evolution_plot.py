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