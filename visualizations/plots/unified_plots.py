import plotly.graph_objects as go
import numpy as np
import pandas as pd
from mpmath import zetazero

def create_analysis_plots(df, stats):
    # Grafico per ogni file
    for file_key in df["File Key"].unique():
        file_df = df[df["File Key"] == file_key]
        fig = go.Figure()
        for _, row in file_df.iterrows():
            fig.add_trace(go.Scatter(
                x=[row["Detected Freq"]], y=[row["Correlation"]],
                mode="markers+text", name=f"{row['Harmonic']} - {row['Critical']}",
                text=[f"{row['Harmonic']}: {row['Correlation']:.2f}"],
                textposition="top center"
            ))
        fig.update_layout(
            title=f"Analisi {file_key}",
            xaxis_title="Frequenza Rilevata (Hz)",
            yaxis_title="Correlazione Critica (C)",
            template="plotly_white"
        )
        fig.write_image(f"{file_key}_analysis.png")

    # Istogramma distribuzione
    f_scaled = df["Detected Freq"] / df["Theoretical Freq"] * 14.1347
    z_zeros = [float(zetazero(i).imag) for i in range(1, 11)]
    fig_dist = go.Figure()
    fig_dist.add_trace(go.Histogram(x=f_scaled, nbinsx=50, name="Frequenze Scalate", opacity=0.7))
    fig_dist.add_trace(go.Histogram(x=z_zeros, nbinsx=50, name="Zeri Zeta", opacity=0.5))
    fig_dist.update_layout(
        title="Distribuzione Frequenze Scalate vs Zeri Zeta",
        xaxis_title="Valore Scalato",
        yaxis_title="Conteggio",
        barmode="overlay",
        annotations=[dict(x=0.9, y=0.9, xref="paper", yref="paper",
                          text=f"KS p-value: {stats['ks_pvalue']:.3f}", showarrow=False)]
    )
    fig_dist.write_image("validation_summary_6205.png")

if __name__ == "__main__":
    df = pd.read_csv("../../backend/simulations/validation_summary_6205.csv")
    with open("../../backend/simulations/validation_stats.json", "r") as f:
        import json
        stats = json.load(f)
    create_analysis_plots(df, stats)