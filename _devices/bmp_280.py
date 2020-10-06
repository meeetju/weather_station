import time

import busio
import adafruit_bmp280

from _devices.device import Device, Measurement


class Bmp280(Device):

    SCL_PIN = 5
    SDA_PIN = 3

    def __init__(self):
        self._temperature = Measurement('Temperature', 'C')
        self._pressure = Measurement('Pressure', 'hPa')
        self._i2c = busio.I2C(self.SCL_PIN, self.SDA_PIN)
        self._sensor = adafruit_bmp280.Adafruit_BMP280_I2C(self._i2c)

    def get_measurements(self):
        self._temperature.value = self._poll_for_measurement(self._sensor.temperature)
        self._pressure.value = self._poll_for_measurement(self._sensor.pressure)
        return [self._temperature, self._pressure]

    @staticmethod
    def _poll_for_measurement(measurement):
        result = None

        while result is None:
            result = measurement
            time.sleep(0.1)

        return result