from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import os
import urllib3

app = Flask(__name__) #assign your name 'app'
app.config["MYSQL_HOST"] = os.environ.get('MYSQL') #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ.get('MYSQLUSER')#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ.get('MYSQLPASSWORD')#Password for DB
app.config["MYSQL_DB"] = os.environ.get('MYSQLDB')#Databse being used
app.config['SECRET_KEY'] = 'secret'

mysql = MySQL(app) # What to define 'MySQL' as 'mysql'

def testDB_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO areaTable (first_name, last_name, area_num)  VALUES ('JesusIs', 'WithHer', 74)")
        mysql.connection.commit()
        cur.execute("SELECT * FROM areaTable")
        record_after = cur.fetchall()
        print(record_after)
        m=[]
        for i in record_after:
            for j in i:
                m.append(j)
        cur.close()
        print(m)
        assert('JesusIs') == m[-3]
        assert('WithHer') == m[-2]
        assert(74) == m[-1]

    
def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.222.72.134:5000/")
    assert 200 == r.status

    
def test_negative():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.222.72.134:5000/daemon")
    assert r.status == 404