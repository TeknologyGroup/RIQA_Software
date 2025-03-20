from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SimulationResult(Base):
    __tablename__ = 'simulation_results'
    
    id = Column(Integer, primary_key=True)
    simulation_type = Column(String, nullable=False, index=True)
    parameters = Column(String, nullable=False)  # JSON string
    results = Column(String, nullable=False)     # JSON string

    # Indice per velocizzare le ricerche per tipo di simulazione
    __table_args__ = (Index('idx_simulation_type', 'simulation_type'),)

    def to_dict(self):
        """Converte il modello in un dizionario."""
        return {
            'id': self.id,
            'simulation_type': self.simulation_type,
            'parameters': self.parameters,
            'results': self.results
        }