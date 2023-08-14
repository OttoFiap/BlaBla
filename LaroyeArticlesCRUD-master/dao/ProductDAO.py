from model.Product import Product
from connection.database_connection import create_connection

class ProductDAO:
    def __init__(self, connection):
        self.connection = create_connection
