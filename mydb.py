import mysql.connector # type: ignore

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE Tally")

print("All Done!!")

