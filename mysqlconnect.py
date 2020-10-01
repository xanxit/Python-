import mysql.connector#need to install using pip install mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='host number',#usually host number is the server number
                                         database='db number',
                                         user='username',
                                         password='password')#adding details of db
    if connection.is_connected():
        db_Info = connection.get_server_info()#geting information of db
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()#creating a cursor for the db usage
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:#error
    print("Error while connecting to MySQL", e)
connection.close()#to close the db!
