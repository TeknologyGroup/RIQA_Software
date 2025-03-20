#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Algoritmo Python per l'integrazione Riemann-Quantum
'''

import argparse
import logging
import numpy as np
import matplotlib.pyplot as plt

# Configurazione del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("RiemannQuantum")

def simulate(t_min=0, t_max=100, steps=10):
    '''Simula un processo (placeholder).'''
    t_values = np.linspace(t_min, t_max, steps)
    # Qui andrebbe il codice di simulazione vero e proprio
    logger.info(f"Simulazione eseguita da t={t_min} a t={t_max} con {steps} passi.")
    plt.plot(t_values, np.sin(t_values)) # Esempio di plot
    plt.xlabel("Tempo")
    plt.ylabel("Valore")
    plt.title("Simulazione Riemann-Quantum (Esempio)")
    plt.savefig("results/simulation_example.png") # Salva in results/
    plt.close()
    return t_values

def main():
    '''Funzione principale per l'esecuzione da CLI.'''
    parser = argparse.ArgumentParser(description='Riemann-Quantum Integration CLI')
    parser.add_argument('command', choices=['simulate'], help='Comando da eseguire')
    parser.add_argument('--t-min', type=float, default=0, help='Valore minimo di t')
    parser.add_argument('--t-max', type=float, default=100, help='Valore massimo di t')
    parser.add_argument('--steps', type=int, default=10, help='Numero di passi nella simulazione')

    args = parser.parse_args()

    if args.command == 'simulate':
        simulate(args.t_min, args.t_max, args.steps)
    else:
        logger.error("Comando non valido.")

if __name__ == "__main__":
    main()
