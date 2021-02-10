from mock import patch, Mock
from unittest import TestCase, main

from weather_station._database._database import Database


class TestDatabase(TestCase):

    def test_database_initialization(self):
        database = Database('my.db')

        self.assertEqual(database._db_file_path, 'my.db', 'File name is correct')

    def test_database_connection_context_manager(self):
        with patch('weather_station._database._database.sqlite3') as mock_sql:
            connection = Mock()
            mock_sql.connect.return_value = connection

            database = Database('my.db')

            with database.connection():
                pass

        self.assertEqual(connection, database._connection, 'Connection was established')
        connection.close.assert_called_once()

    def test_database_connection_error(self):
        with patch('weather_station._database._database.logging') as mock_logging:
            database = Database('1:\my.db')
            database.connect()

        mock_logging.error.assert_called_once_with('Connection error occurred: unable to open database file')


if __name__ == '__main__':
    main()