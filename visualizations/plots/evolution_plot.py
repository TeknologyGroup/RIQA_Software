import plotly.graph_objects as go

def create_evolution_plot(time, frequency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=frequency, mode='lines', name='Frequenza Allelica'))
    fig.update_layout(title="Simulazione Evolutiva", xaxis_title="Tempo", yaxis_title="Frequenza Allelica")
    return fig
