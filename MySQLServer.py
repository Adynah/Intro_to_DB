import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",     #Fake password
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Exception as e:
    print("Error: Failed to connect to Database")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
