import logging
import time

from _sensors.dht_11 import Dht11
from _sensors.bmp_280 import Bmp280

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main():

    dht11 = Dht11()
    bmp280 = Bmp280()
    devices = [dht11, bmp280]

    while True:
         for device in devices:
             measurements = device.get_measurements()
             for measurement in measurements:
                 logging.info(measurement)

         time.sleep(1)


if __name__ == '__main__':
    main()