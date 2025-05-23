
from flask import Flask, render_template, jsonify
import time
import board
import busio
import adafruit_ccs811
import adafruit_bme280
from adafruit_bme280 import basic as adafruit_bme280
import os
from datetime import datetime

app = Flask(__name__)

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c, address=0x5b)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

DATA_FILE = 'sensor_data.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    co2 = ccs811.eco2
    tvoc = ccs811.tvoc
    temperature = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure

    # Append to data file
    timestamp = datetime.now().isoformat()
    with open(DATA_FILE, 'a') as f:
        f.write(f"{timestamp},{temperature:.2f},{humidity:.2f},{pressure:.2f},{co2},{tvoc}\n")

    return jsonify(co2=co2, tvoc=tvoc, temperature=temperature,
                   humidity=humidity, pressure=pressure)

@app.route('/get_history')
def get_history():
    if not os.path.exists(DATA_FILE):
        return jsonify({})

    with open(DATA_FILE, 'r') as f:
        lines = f.readlines()

    # Get current date in ISO format (YYYY-MM-DD)
    current_date = datetime.now().date().isoformat()

    # Group data by hour for the current date
    hourly_data = {}
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 6:
            timestamp, temperature, humidity, pressure, co2, tvoc = parts
            try:
                dt = datetime.fromisoformat(timestamp)
            except ValueError:
                continue
            if dt.date().isoformat() == current_date:  # Check if the date matches the current date
                hour = dt.hour

                if hour not in hourly_data:
                    hourly_data[hour] = {'temps': [], 'humidities': []}

                hourly_data[hour]['temps'].append(float(temperature))
                hourly_data[hour]['humidities'].append(float(humidity))

    # Calculate averages
    hourly_averages = {}
    for hour in range(24):  # Ensure all 24 hours are included
        if hour in hourly_data:
            temps = hourly_data[hour]['temps']
            humidities = hourly_data[hour]['humidities']
            hourly_averages[hour] = {
                'temperature': sum(temps) / len(temps) if temps else None,
                'humidity': sum(humidities) / len(humidities) if humidities else None
            }
        else:
            hourly_averages[hour] = {
                'temperature': None,
                'humidity': None
            }

    return jsonify(hourly_averages)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
