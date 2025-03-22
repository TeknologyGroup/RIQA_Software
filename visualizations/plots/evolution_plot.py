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
    
    # opzioni di personalizzazione per i grafici, come la scelta di colori, stili e temi.#

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
    
    #animazioni per mostrare l'evoluzione dei dati nel tempo.
    def create_animated_evolution_plot(time: list, frequency: list) -> go.Figure:
    """
    Crea un grafico animato dell'evoluzione allelica.

    Args:
        time: Lista dei tempi.
        frequency: Lista delle frequenze alleliche.

    Returns:
        Oggetto Figure di Plotly con animazione.
    """
    fig = go.Figure()

    # Aggiungi traccia animata
    fig.add_trace(go.Scatter(
        x=time,
        y=frequency,
        mode='lines',
        name='Frequenza Allelica',
        line=dict(color='royalblue', width=2)
    ))

    # Aggiungi fotogrammi per l'animazione
    frames = [go.Frame(data=[go.Scatter(x=time[:i], y=frequency[:i]) for i in range(1, len(time))]

    # Configura l'animazione
    fig.frames = frames
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                         method="animate",
                         args=[None, {"frame": {"duration": 100, "redraw": True}}])],
            direction="left",
            showactive=False,
            x=1.0,
            y=1.1
        )]
    )

    return fig

    ### **Aggiunta di Opzioni di Esportazione**###

#Implementa l'esportazione dei grafici in formati come PDF e SVG, oltre a PNG
import plotly.graph_objects as go
import plotly.io as pio

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

    # Aggiungi pulsanti per esportare in PNG, PDF e SVG
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[
                dict(label="Esporta PNG",
                     method="download_image",
                     args=["evolution_plot.png", "png"]),
                dict(label="Esporta PDF",
                     method="download_image",
                     args=["evolution_plot.pdf", "pdf"]),
                dict(label="Esporta SVG",
                     method="download_image",
                     args=["evolution_plot.svg", "svg"])
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


### **Personalizzazione Avanzata** ###

#Aggiungi più opzioni di personalizzazione, come la scelta di colori, stili e temi

def create_evolution_plot(time: list, frequency: list, theme: str = 'plotly_white', line_color: str = 'royalblue') -> go.Figure:
    """
    Crea un grafico interattivo dell'evoluzione allelica con personalizzazione avanzata.

    Args:
        time: Lista dei tempi.
        frequency: Lista delle frequenze alleliche.
        theme: Tema del grafico (es. 'plotly', 'plotly_white', 'plotly_dark').
        line_color: Colore della linea del grafico.

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
        line=dict(color=line_color, width=2, dash='solid'),
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

    # Aggiungi pulsanti per esportare in PNG, PDF e SVG
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[
                dict(label="Esporta PNG",
                     method="download_image",
                     args=["evolution_plot.png", "png"]),
                dict(label="Esporta PDF",
                     method="download_image",
                     args=["evolution_plot.pdf", "pdf"]),
                dict(label="Esporta SVG",
                     method="download_image",
                     args=["evolution_plot.svg", "svg"])
            ],
            direction="left",
            showactive=False,
            x=1.0,
            y=1.1
        )]
    )

    return fig
