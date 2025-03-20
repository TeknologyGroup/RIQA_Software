import serial
from database.models.simulation_results import SimulationResult
from sqlalchemy.orm import Session
from database.base import engine

# Configurazione della porta seriale (adatta al tuo sistema)
SERIAL_PORT = '/dev/ttyUSB0'  # Su Linux/Mac; su Windows usa 'COMX'
BAUD_RATE = 9600

def save_to_database(data: str):
    """Salva i dati ricevuti nel database."""
    with Session(engine) as session:
        result = SimulationResult(
            simulation_type="mobile_sensor",
            parameters="Bluetooth data",
            results=data
        )
        session.add(result)
        session.commit()

def read_from_bluetooth():
    """Legge dati dal modulo Bluetooth collegato ad Arduino."""
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("Connessione Bluetooth stabilita...")
        
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                print(f"Dato ricevuto: {data}")
                save_to_database(data)
                
    except serial.SerialException as e:
        print(f"Errore seriale: {e}")
    finally:
        if 'ser' in locals():
            ser.close()

if __name__ == "__main__":
    read_from_bluetooth()