import plotly.graph_objects as go
import numpy as np

def create_wormhole_plot(r, b_r, Phi_r, b0, t_n):
    fig = go.Figure()
    
    # Traccia b(r)
    fig.add_trace(go.Scatter(
        x=r, y=b_r, mode='lines', name='Funzione di forma b(r)',
        line=dict(color='blue', width=2)
    ))
    
    # Traccia Phi(r)
    fig.add_trace(go.Scatter(
        x=r, y=Phi_r, mode='lines', name='Potenziale Φ(r)',
        line=dict(color='red', width=2, dash='dash')
    ))
    
    # Linea della gola
    fig.add_vline(x=b0, line=dict(color='gray', dash='dot'), annotation_text=f'b0 = {b0:.2f}')
    
    fig.update_layout(
        title=f"Profilo Wormhole con Zero Zeta t_n = {t_n:.2f}",
        xaxis_title="Coordinata radiale r",
        yaxis_title="Valore",
        template="plotly_white",
        hovermode="x unified",
        showlegend=True
    )
    
    return fig

# Esempio di utilizzo con i dati della simulazione
if __name__ == "__main__":
    from backend.simulations.wormhole_zeta import WormholeZetaSimulation
    sim = WormholeZetaSimulation(zero_index=1)
    data = sim.calculate_metric()
    fig = create_wormhole_plot(data['r'], data['b_r'], data['Phi_r'], data['b0'], data['t_n'])
    fig.show()