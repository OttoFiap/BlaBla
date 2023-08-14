from pyodbc import connect, Error


def create_connection():
    try:
        # Credentials For Connection With Database
        connection_data = 'Driver={SQLite3 ODBC Driver};Database=..\connection\LaroyeStore.db'
        connection = connect(connection_data)
        # Connection Success Message
        print('\033[92mConnected with database successfully!\033[0m')
        return connection
    except Error as e:
        print(f'\033[91mError while trying to connect with database: {e}\033[0m')
        return None

