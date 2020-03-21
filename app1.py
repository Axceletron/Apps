import mysql.connector
from mysql.connector import Error
from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mn=connect()
    return str(mn)

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host= os.getenv('HOST'),
                                       database= os.getenv('DB_NAME'),
                                       user= os.getenv('USER'),
                                       password= os.getenv('PASSWORD'))
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
 
 
if __name__ == '__main__':
    connect()
    app.run(host="0.0.0.0", port=8000, debug=True)