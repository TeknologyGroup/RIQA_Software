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