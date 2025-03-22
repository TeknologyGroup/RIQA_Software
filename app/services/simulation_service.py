# app/services/simulation_service.py
from sqlalchemy.orm import Session
from app.models.simulation import SimulationResult

def get_simulation_results_by_type(session: Session, simulation_type: str):
    return session.query(SimulationResult).filter(SimulationResult.simulation_type == simulation_type).all()
