from connection.database_connection import create_connection


# Function That Verifies If User's Credentials Are Correct
def verify_credentials(username, password):
    # Getting Database Connection
    connection = create_connection()
    # Creating a Cursor To Make Query
    cursor = connection.cursor()
    # Executing Query From The Cursor
    cursor.execute('''SELECT * 
                      FROM User
                      WHERE name = ?        
                      AND password = ?''', (username, password))
    # Storing Query Return
    user = cursor.fetchone()
    # Conferring If The Credentials Inserted Are Registered
    if user:
        return True
    else:
        return False
