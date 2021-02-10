from unittest import TestCase, main

from weather_station._sensors.sensor import Measurement


class TestSensors(TestCase):

    def test_measurement_initialized_properly(self):

        measurement = Measurement('Current', 'mA')

        self.assertEqual(measurement.name, 'Current', 'Name is correct')
        self.assertEqual(measurement.unit, 'mA', 'Unit is correct')
        self.assertEqual(measurement.value, -1000.0, 'Value is default')

    def test_setting_measurement_value(self):

        measurement = Measurement('Current', 'mA')
        measurement.value = 123

        self.assertEqual(measurement.value, 123, 'Value is correct')


if __name__ == '__main__':
    main()
