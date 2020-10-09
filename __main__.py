# encoding: utf-8"

from datetime import date, datetime
import logging
import time


from _sensors.dht_11 import Dht11
from _sensors.bmp_280 import Bmp280
from _database._database import Database, SQL_CREATE_MEASUREMENTS_TABLE, SQL_INSERT_QUERY

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main():

    dht11 = Dht11()
    bmp280 = Bmp280()

    database = Database('./weather_data.db')
    database.create_table(SQL_CREATE_MEASUREMENTS_TABLE)

    while True:
        dt = datetime.utcnow()
        humidity = dht11.get_measurements()[0]
        logging.info(humidity)
        temperature, pressure = bmp280.get_measurements()
        logging.info(temperature)
        logging.info(pressure)
        database.insert_to_table(SQL_INSERT_QUERY, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, humidity.value, temperature.value, pressure.value)
        time.sleep(5)


if __name__ == '__main__':
    main()