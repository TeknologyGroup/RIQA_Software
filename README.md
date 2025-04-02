# RIQA_Software

**Subtitle**: Wormhole Simulation and Riemann Zeta Function Zeros
**Author**: Martino Battista
**Date**: March 20, 2025
**License**: MIT License

---

## Overview

**RIQA_Software** is a modular open-source framework designed to explore the theoretical connection between traversable wormholes in general relativity and the non-trivial zeros of the Riemann zeta function ($$ \zeta(s) $$). The project integrates numerical simulations, interactive 2D and 3D visualizations, data collection from physical sensors, and a voice interface, offering a versatile tool for interdisciplinary research between theoretical physics and pure mathematics.

The central hypothesis proposes that the non-trivial zeros of $$ \zeta(s) $$ on the critical line ($$ s = 1/2 + it $$, e.g., $$ t_1 \approx 14.1347 $$) may correspond to singularities or critical points in the wormhole metric, suggesting a relationship between the distribution of prime numbers and the geometry of spacetime.

## Key Features

- **Numerical Simulations**: Calculation of the wormhole metric with parameters influenced by the zeros of $$ \zeta(s) $$.
- **Visualizations**: Interactive 2D charts (Plotly) and dynamic 3D models (Three.js) of the wormhole geometry.
- **Hardware Integration**: Real-time data collection from sensors (e.g., MPU-6050 accelerometer) via Bluetooth Low Energy (BLE).
- **Voice Control**: Assistant interface to start simulations with voice commands.
- **Database**: Structured storage of results and experimental data with SQLite.

## Project Structure

The repository structure is organized in a modular way to clearly separate the different components:

```plaintext
RIQA_Software/
├── frontend/                  # React-based user interface
│   ├── src/                   # Frontend source code
│   │   ├── App.js             # Application routing and main layout
│   │   ├── components/        # Reusable React components
│   │   │   ├── SimulationForm.js  # Form to start and configure simulations
│   │   │   └── Wormhole3D.js      # 3D wormhole visualization with Three.js
│   │   └── pages/             # Application pages
│   │       └── Simulations.js     # Page dedicated to simulations
├── backend/                   # Flask server for logic and API
│   ├── main.py                # Main Flask API file
│   ├── simulations/           # Modules for simulations
│   │   └── wormhole_zeta.py # Wormhole metric simulation based on zeta zeros
│   ├── assistant_interface.py # Voice interface for software control
│   └── mobile_data.py         # Management of data received from sensors via Bluetooth/BLE
├── database/                 # SQLite database for data and results
│   └── models/               # Data models
│       └── simulation_results.py  # Database schema for simulation results
├── visualizations/           # Tools for data visualization
│   └── plots/                # Modules for charts
│       └── wormhole_plot.py # Interactive 2D plots of the metric with Plotly
├── hardware/                 # Integration with hardware devices
│   └── mobile_integration/   # Communication with mobile devices
│       ├── bluetooth/        # Scripts for Bluetooth and BLE
│       │   └── arduino_hm10_sensors.ino  # Arduino code for HM-10 and sensors
│       └── mobile_app/       # Mobile application
│           └── main.dart     # Flutter app for control and monitoring
├── docs/                     # Project documentation
│   ├── wormhole_zeta.md      # Theory on wormholes and zeta function zeros
│   ├── formulas.tex          # Collection of mathematical formulas in LaTeX
└── requirements.txt          # List of Python dependencies
```

## Prerequisites

- **Python**: 3.8 or higher
- **Node.js**: For the React frontend
- **Flutter**: For the mobile app (iOS/Android)
- **Arduino IDE**: To upload code to hardware devices
- **Hardware**: Arduino with HM-10 module and MPU-6050 sensor (optional)

## Installation

To start the **RIQA_Software** project on a Linux (Debian) terminal on a Chromebook, follow these steps. Make sure you have already configured the Linux environment on your Chromebook and have installed the necessary prerequisites (Python, Node.js, Flutter, Arduino IDE, etc.).

---

### **1. Clone the Repository**
Open the Linux terminal and clone the project's GitHub repository:

```bash
git clone https://github.com/[your-username]/RIQA_Software.git
cd RIQA_Software
```

Replace `[your-username]` with your GitHub username or the correct repository URL.

---

### **2. Install Backend Dependencies**
Install the necessary Python dependencies for the Flask backend:

```bash
pip install -r requirements.txt
```

If you don't have `pip` installed, you can install it with:

```bash
sudo apt update
sudo apt install python3-pip
```

---

### **3. Start the Backend**
Start the Flask server for the backend:

```bash
python backend/main.py
```

The Flask server should start and remain running, awaiting requests. Keep this terminal open.

---

### **4. Install Frontend Dependencies**
Open a new terminal (or a new terminal tab) and navigate to the `frontend` folder:

```bash
cd frontend
```

Install the Node.js dependencies for the React frontend:

```bash
npm install
```

Also install the `three.js` library for the 3D visualizations:

```bash
npm install three
```

---

### **5. Start the Frontend**
Start the React development server:

```bash
npm start
```

This will automatically open the frontend in the default browser at `http://localhost:3000`. If it doesn't open automatically, you can access it manually.

---

### **6. Configure Hardware (Optional)**
If you want to use the hardware (Arduino with HM-10 module and MPU-6050 sensor), follow these steps:

1. **Upload Code to Arduino**:
   - Open the file `hardware/mobile_integration/bluetooth/arduino_hm10_sensors.ino` in the Arduino IDE.
   - Connect the Arduino to the Chromebook and upload the code.

2. **Start Data Management**:
   Return to the main terminal (where you cloned the repository) and start the Python script for data management:

   ```bash
   python backend/mobile_data.py
   ```

---

### **7. Configure the Mobile App (Optional)**
If you want to use the Flutter mobile app:

1. Install Flutter on your Chromebook (if you haven't already):
   - Follow the official guide: https://flutter.dev/docs/get-started/install/linux

2. Navigate to the mobile app folder:

   ```bash
   cd hardware/mobile_integration/mobile_app/
   ```

3. Install the Flutter dependencies:

   ```bash
   flutter pub get
   ```

4. Run the app:

   ```bash
   flutter run
   ```

---

### **8. Using the Software**
Now that everything is set up, you can use the software:

1. **Frontend**:
   - Open `http://localhost:3000` in your browser.
   - Go to the "Simulations" page and enter an index of a non-trivial zero (e.g., "1" for $$ t_1 \approx 14.1347 $$) in the form.
   - Click "Run Simulation" to start the simulation.

2. **Visualization**:
   - The 2D plots of the metric will be displayed with Plotly.
   - The interactive 3D model of the wormhole will be displayed with Three.js.

3. **Hardware Data**:
   - If you have configured the hardware, the sensor data will be collected and correlated with the simulation parameters.

---

### **9. Debugging and Troubleshooting**
- If you encounter errors, verify that all dependencies are installed correctly.
- Check that the Flask and React servers are running.
- If you are using the hardware, make sure the Arduino is correctly connected and configured.

---

### **10. Stopping the Services**
To stop the services:
- Press `Ctrl + C` in the terminals where Flask (`backend/main.py`) and React (`npm start`) are running.

---

By following these steps, you should be able to start and use the **RIQA_Software** project on your Chromebook with Linux Debian.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/39375871/b51c465b-1f7f-4aa0-b58b-f04007549a1c/paste.txt

---
Risposta da Perplexity: pplx.ai/share
