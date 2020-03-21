from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    data=""

    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)