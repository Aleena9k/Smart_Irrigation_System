#include <DHT.h>

// Define pins
#define DHTPIN 2         // DHT11 data pin
#define DHTTYPE DHT11
#define SOIL_PIN A0      // Soil moisture sensor
#define RELAY_PIN 7      // Relay module

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(SOIL_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  digitalWrite(RELAY_PIN, LOW); // Motor OFF by default
}

void loop() {
  // Read sensors
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilMoisture = analogRead(SOIL_PIN);

  // Check if readings are valid
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Sensor error");
    delay(2000);
    return;
  }

  // Send data over serial
  Serial.print(temperature, 2);
  Serial.print(",");
  Serial.print(humidity, 2);
  Serial.print(",");
  Serial.println(soilMoisture);

  // Wait for Python response
  unsigned long start = millis();
  while (millis() - start < 5000) { // wait up to 5 sec
    if (Serial.available()) {
      char command = Serial.read();
      if (command == 'W') {
    digitalWrite(RELAY_PIN, LOW);  // Motor ON
}else if (command == 'N') {
    digitalWrite(RELAY_PIN, HIGH);   // Motor OFF
}
      break;
    }
  }

  delay(5000); // Delay before next reading
}
