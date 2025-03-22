# app/models/simulation.py
from sqlalchemy import Index

class SimulationResult(Base):
    __tablename__ = 'simulation_results'
    id = Column(Integer, primary_key=True)
    simulation_type = Column(String, nullable=False, index=True)
    parameters = Column(String, nullable=False)
    results = Column(String, nullable=False)
    description = Column(String)

# Crea un indice composto se necessario
Index('idx_simulation_type_description', SimulationResult.simulation_type, SimulationResult.description)

# app/models/simulation.py
from sqlalchemy import Column, Integer, String, Float
from database.base import Base

class SimulationResult(Base):
    """
    Modello per i risultati delle simulazioni.

    Attributi:
        id (int): ID unico del risultato.
        simulation_type (str): Tipo di simulazione.
        parameters (str): Parametri della simulazione in formato JSON.
        results (str): Risultati della simulazione in formato JSON.
        description (str): Descrizione opzionale del risultato.
    """
    __tablename__ = 'simulation_results'
    id = Column(Integer, primary_key=True)
    simulation_type = Column(String, nullable=False)
    parameters = Column(String, nullable=False)
    results = Column(String, nullable=False)
    description = Column(String)
