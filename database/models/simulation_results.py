from sqlalchemy import Column, Integer, Float, String
from database.base import Base

class SimulationResult(Base):
    __tablename__ = 'simulation_results'
    id = Column(Integer, primary_key=True)
    simulation_type = Column(String)
    parameters = Column(String)
    results = Column(String)
