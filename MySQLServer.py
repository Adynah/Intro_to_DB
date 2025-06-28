import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",     #Fake password
        database="alx_book_store"
    )

    if mydb.is_connected():
        print("Database 'alx_book_store' created successfully!")

except Error as err:
    print(f"Error: {err}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
