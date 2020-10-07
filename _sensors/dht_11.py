import time

import Adafruit_DHT
from _sensors.sensor import Sensor, Measurement


class Dht11(Sensor):

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

    def __init__(self):
        self._humidity = Measurement('Humidity', '%')

    def get_measurements(self):
        self._humidity.value = self._poll_for_measurements()
        return [self._humidity]

    def _poll_for_measurements(self):
        humidity = None

        while humidity is None:
            humidity, _ = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            time.sleep(0.1)

        return humidity
