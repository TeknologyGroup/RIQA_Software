import serial
from database.models.simulation_results import SimulationResult
from sqlalchemy.orm import Session
from database.base import engine
from backend.simulations.wormhole_zeta import WormholeZetaSimulation

# Configurazione della porta seriale (adatta al tuo sistema)
SERIAL_PORT = '/dev/ttyUSB0'  # Su Linux/Mac; su Windows usa 'COMX'
BAUD_RATE = 9600

def save_to_database(data: str, session: Session):
    """
    Salva i dati ricevuti nel database e correla con la simulazione wormhole.
    
    Args:
        data: Stringa ricevuta dal sensore (es. "ACCEL:9.81").
        session: Sessione SQLAlchemy attiva.
    """
    simulation_type = "unknown"
    parameters = "N/A"
    value = data

    # Interpreta i dati del sensore
    if "ACCEL:" in data:
        simulation_type = "sensor_data"
        parameters = "Accelerazione gravitazionale (m/s^2)"
        try:
            value = float(data.split("ACCEL:")[1])
        except (IndexError, ValueError):
            value = 0.0

    # Salva nel database
    result = SimulationResult(
        simulation_type=simulation_type,
        parameters=parameters,
        results=str(value)
    )
    session.add(result)
    session.commit()

    # Correlazione con simulazione wormhole
    if simulation_type == "sensor_data":
        sim = WormholeZetaSimulation(zero_index=1)  # Usa il primo zero per default
        metric = sim.calculate_metric()
        print(f"Correlazione: Accelerazione={value} m/s^2, b0={metric['b0']:.2f}")

def read_from_bluetooth():
    """
    Legge dati dal modulo Bluetooth/BLE e li elabora.
    """
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connessione Bluetooth stabilita su {SERIAL_PORT}")
        
        with Session(engine) as session:
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    if data:
                        print(f"Dato ricevuto: {data}")
                        save_to_database(data, session)
                
    except serial.SerialException as e:
        print(f"Errore seriale: {e}")
    except KeyboardInterrupt:
        print("Interruzione manuale")
    finally:
        if 'ser' in locals():
            ser.close()
            print("Connessione seriale chiusa")

if __name__ == "__main__":
    read_from_bluetooth()