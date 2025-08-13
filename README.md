# Raspberry Pi Weather and Air Quality Monitor

## About

Raspberry Pi Weather and Air Quality Monitor is a real-time environmental monitoring system using a Raspberry Pi and multiple sensors to track air quality (CO₂, TVOC), temperature, humidity, and atmospheric pressure. 

The data is served through a Flask web application and displayed on a dynamic, auto-updating frontend.

<img src="https://github.com/user-attachments/assets/c2e5ffe8-53d1-4ec7-bebd-9167ea19795f" width="300" />
<img src="https://github.com/user-attachments/assets/4022a870-6de5-4d0a-baf2-9aed87179919" width="300" />
<img src="https://github.com/user-attachments/assets/ea78489f-6f76-403a-9e10-f520d310b6c8" width="300" />

## Features

-🌫️ Real-time CO₂ and TVOC readings

-🌡️ Temperature, humidity, and pressure monitoring

-🧠 Flask-based backend with live API (/get_data)

-🌐 Responsive frontend with auto-refreshing values (every 2 seconds)

-📝 Data logging to sensor_data.txt with timestamps

## Demo

Access the application from your Raspberry Pi or any device on the same network:

```http://<your-ip>:5000/```

Example:

```http://192.168.1.100:5000/```

## Getting Started

### Prerequisites

Make sure you have the following:

- Raspberry Pi 4 (or compatible)
- Raspberry Pi OS Lite installed
- Python 3 and pip
- Internet connection (for installing packages)
- WPSE342 Sensor
- Breadboard, jumper wires (male-female)

### Wiring

| Sensor Pin | Raspberry Pi Pin |
|------------------|------------------|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO 2 (SDA) |
| SCL | GPIO 3 (SCL) |
| WAKE | GPIO 4 |

### Installation

1. Enable I2C on your Raspberry Pi:
```bash
 sudo raspi-config
```
 > Navigate to Interfacing Options > I2C > Enable.
2. Install dependencies:
```bash
 sudo apt update
 sudo apt install python3-pip i2c-tools
 pip3 install --break-system-packages flask adafruit-circuitpython-ccs811 adafruit-circuitpython-bme280

```
3. Clone or copy this project:
```bash
 git clone https://github.com/idleCyrex/raspberry-pi-weather-air-quality-monitor.git
 cd raspberry-pi-weather-air-quality-monitor
```
4. Run the application:
```bash
 python3 app.py
```
5. Open your browser and go to:
   
 ```
 http://<your-raspberry-pi-ip>:5000/
```


### File Structure

     app.py # Flask backend (main file)
          templates/
               index.html # Frontend UI
          static/
               style.css # Optional custom styles
     sensor_data.txt # Auto-generated data log

## Notes

- Make sure the sensor is properly connected and detected using `i2cdetect -y 1`
- All sensor data is logged to `sensor_data.txt` every time the API is called
- Page auto-refreshes every 2 seconds using JavaScript fetch()

---

## License

This project was created for educational purposes. You are free to reuse or modify it as needed.
