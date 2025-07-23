import pickle
import serial
import time
import numpy as np

# Load ML Model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load Scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Setup serial communication (change COM port as needed)
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Allow Arduino to initialize

print("Listening for sensor data...")

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            print("Data from Arduino:", line)

            try:
                # Arduino sends: Temperature,Humidity,SoilMoisture
                values = list(map(float, line.split(',')))

                if len(values) == 3:
                    temperature, humidity, soil_moisture = values
                    features = [temperature, humidity, soil_moisture]

                    # Scale and predict
                    features_scaled = scaler.transform([features])
                    prediction = model.predict(features_scaled)[0]

                    # Respond based on prediction
                    if prediction == 1:
                        print("Prediction: ON")
                        ser.write(b'W')  # Command to turn on motor
                        print("Action: Watering (Pump ON)")
                    else:
                        print("Prediction: OFF")
                        ser.write(b'N')  # Command to turn off motor
                        print("Action: Not Watering (Pump OFF)")
                else:
                    print("Invalid input format")

            except Exception as e:
                print("Error:", e)

        time.sleep(5)  # Wait before checking again

except KeyboardInterrupt:
    print("\nInterrupted by user. Exiting...")

finally:
    print("Turning off motor before exiting...")
    ser.write(b'N')  # Ensure motor is OFF
    time.sleep(1)    # Give Arduino time to process the command
    ser.close()
