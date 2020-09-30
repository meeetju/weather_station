import time

import Adafruit_DHT
from _devices.device import Device, Measurement


class Dht11(Device):

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

    def __init__(self):
        self._temperature = Measurement('Temperature', 'C')
        self._humidity = Measurement('Humidity', '%')

    def get_measurements(self):
        self._humidity.value, self._temperature.value = self._poll_for_measurements()
        return [self._temperature, self._humidity]

    def _poll_for_measurements(self):
        humidity = None
        temperature = None

        while humidity is None or temperature is None:
            humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            time.sleep(0.1)

        return humidity, temperature

