import mysql.connector
from mysql.connector import Error
import sys
import invertedindex

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sys',
                                         user='root',
                                         password='Anurag@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database uploaded")
        invertedindex.func(sys.argv[1], sys.argv[2],connection)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")