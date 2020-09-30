import logging
import time

from _devices.dht_11 import Dht11

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main():

    dht11 = Dht11()
    devices = [dht11]

    while True:
         for device in devices:
             measurements = device.get_measurements()
             for measurement in measurements:
                 logging.info(measurement.get())

         time.sleep(1)


if __name__ == '__main__':
    main()