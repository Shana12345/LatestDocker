from application import app
from flask import Flask, render_template, request, url_for, redirect, flash, Flask
from flask_mysqldb import MySQL 
import requests
import random
import os

app = Flask(__name__) #assign your name 'app'
app.config["MYSQL_HOST"] = os.environ['MYSQL'] #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ['MYSQLUSER']#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASSWORD']#Password for DB
app.config["MYSQL_DB"] = os.environ['MYSQLDB'] #Databse being used
app.config['SECRET_KEY'] = 'secret'
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomName')
    print(response)
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/Fordetails', methods=['GET', 'POST'])
def Fordetails():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        CusDetails=request.form
        first_name=CusDetails['first_name']
        last_name=CusDetails['last_name']
        area_num=CusDetails['area_num']
        cur.execute("INSERT INTO areaTable (first_name, last_name, area_num) VALUES(%s, %s, %s)", [first_name, last_name, area_num])
        mysql.connection.commit()  
        cur.close()
    return render_template('index.html')
        

