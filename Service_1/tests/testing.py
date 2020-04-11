from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import os
import urllib3

app = Flask(__name__) #assign your name 'app'
app.config["MYSQL_HOST"] = os.environ['MYSQL'] #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ['MYSQLUSER']#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASSWORD']#Password for DB
app.config["MYSQL_DB"] = os.environ['MYSQLDB'] #Databse being used

mysql = MySQL(app) # What to define 'MySQL' as 'mysql'

def test_url():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.89.56.7:5000/')
    assert 200 == r.status


def test_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO areaTable (first_name, last_name, area_num)  VALUES ('Hannah', 'Montana', 7)")
        mysql.connection.commit()
        cur.execute("SELECT * FROM areaTable") #this gets record after update
        record_after = cur.fetchall()
        print(record_after)
        m=[]
        for i in record_after:
            for j in i:
                m.append(j)
        cur.close()
    print(m)
     
    assert('Hannah') == m[-3]
    assert('Montana') == m[-2]
    assert(7) == m[-1]

def test_example(dockerc):
    assert len(dockerc.containers()) == 1
    container = dockerc.containers()[0]
    assert container.is_running is True
    assert container.labels["com.docker.compose.service"] == "python"