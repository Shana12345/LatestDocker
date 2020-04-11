from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os, random, requests
import json

app = Flask(__name__)
mysql = MySQL(app)
app.config.from_object(__name__)
app.config["MYSQL_HOST"] = os.environ.get('MYSQL') #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ.get('MYSQLUSER')#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ.get('MYSQLPASSWORD')#Password for DB
app.config["MYSQL_DB"] = os.environ.get('MYSQLDB')#Databse being used
app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomName')
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        CusDetails=request.form
        first_name=CusDetails['first_name']
        last_name=CusDetails['last_name']
        area_num=CusDetails['area_num']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("INSERT INTO areaTable (first_name, last_name, area_num) VALUES(%s, %s, %s)", [first_name, last_name, area_num])
        if resultValue > 1:
            flash("submitted sucessfully", 'success')
        mysql.connection.commit()  
        cur.close()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
        

