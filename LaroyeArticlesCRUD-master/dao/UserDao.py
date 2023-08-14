from model.User import User
from connection.database_connection import create_connection

class UserDAO:
    def __init__(self, connection):
        self.connection = create_connection

    def select_all_users(self):
        try:
            query = 'SELECT '  \
                    '    *'    \
                    'FROM '    \
                    '    User'
            with self.connection as connection:
                cursor.execute(query)
                users = cursor.fetchall()
                return [User(*row) for row in users]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mUser\033[0m:\n{e}')


    def select_user_by_name(self, product_name):
        try:
            query = f'SELECT '  \
                    f'    *'    \
                    f'FROM '    \
                    f'    User' \
                    f'WHERE '   \
                    f'    name = {product_name}'
            with self.connection as connection:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return User(*row)
                else:
                    print(f'\033[1;31mThere is no user with name {product_name}.\033[0m')
        except Exception as e:
            print(f'Error While Trying To Select Data From \033[1;31mComment\033[0m With Specific Name:\n{e}')


    def insert_user(self, user):
        with self.connection as cursor:
            try:
                query = f'INSERT INTO '             \
                        f'    User(name, password)' \
                        f'VALUES'                   \
                        f'    ({user.get_user_name()}, {user.get_user_password()})'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in User.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mUser\033[0m:\n{e}')
