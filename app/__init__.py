import os
import sqlalchemy
#source ./env/bin/activate 
from yaml import load, Loader
from flask import Flask, jsonify, render_template
import mysql.connector as mysql

def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=os.environ.get('MYSQL_USER'), #username
                password=os.environ.get('MYSQL_PASSWORD'), #user password
                database=os.environ.get('MYSQL_DB'), #database name
                host=os.environ.get('MYSQL_HOST') #ip
            )
        )
    return pool

db = init_connect_engine()
connection = db.connect()
metadata = sqlalchemy.MetaData()
print(connection)
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from app import routes

"""
def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    db = mysql.connect(
        host=os.environ.get('MYSQL_HOST'), #ip
        database=os.environ.get('MYSQL_DB'), #database name
        user=os.environ.get('MYSQL_USER'), #username
        password=os.environ.get('MYSQL_PASSWORD') #user password
    )
    return db

db = init_connect_engine()

print("Connected to:", db.get_server_info())
cursor = db.cursor()

cursor.execute("Select * from Rating;")
for i in cursor:
    print(i)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from app import routes
"""