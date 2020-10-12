from contextlib import contextmanager
import logging
import sqlite3


class Database():

    """Log and get data."""

    def __init__(self, db_file_path):
        self._db_file_path = db_file_path
        self._connection = None

    def connect(self):
        """Create connection to sqlite database."""
        try:
            self._connection = sqlite3.connect(self._db_file_path)
            logging.info('Connection {} established to {}'.format(self._connection, self._db_file_path))

        except sqlite3.Error as error:
            logging.error('Connection error occurred: {}'.format(error))

    def disconnect(self):
        """Close connection."""
        try:
            self._connection.close()
            logging.info('Connection closed')
        except sqlite3.Error as error:
            logging.error('Connection close error occurred: {}'.format(error))

    @contextmanager
    def connection(self):
        """Connect and disconnect from database."""
        self.connect()
        yield
        self.disconnect()

    def create_table(self, sql_create_table):
        """Create table."""
        with self.connection():
            try:
                cursor = self._connection.cursor()
                cursor.execute(sql_create_table)
                logging.info('Table exists or created')
            except sqlite3.Error as error:
                logging.error('Table create error occurred: {}'.format(error))

    def insert_to_table(self, sql_insert_template, *args):
        with self.connection():
            try:
                insert = sql_insert_template.format(*args)
                logging.info('Insert data {}'.format(insert))
                cursor = self._connection.cursor()
                cursor.execute(insert)
                self._connection.commit()
                logging.info('Inserted data {}'.format(*args))
                cursor.close()
            except sqlite3.Error as error:
                logging.error('Insert error occurred: {}'.format(error))


SQL_CREATE_MEASUREMENTS_TABLE = """ 
CREATE TABLE IF NOT EXISTS measurements (
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
humidity real,
temperature real,
pressure real
);"""

SQL_INSERT_QUERY = """
INSERT INTO measurements
(humidity, temperature, pressure) 
VALUES 
({},{},{})"""