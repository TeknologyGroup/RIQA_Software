import serial

def read_from_arduino(port='/dev/ttyUSB0', baud_rate=9600):
    ser = serial.Serial(port, baud_rate, timeout=1)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print("Received from Arduino:", data)
            # Process or store the data as needed
    ser.close()

# Call this in your Flask app if needed