import pytest
from app.services.sensor_data import process_sensor_data

def test_process_sensor_data():
    sensor_data = "ACCEL:9.81"
    result = process_sensor_data(sensor_data)
    assert result['sensor_type'] == 'sensor_data'
    assert result['value'] == 9.81
