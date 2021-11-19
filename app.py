from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "pes_interconnect2"
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASS']

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST)


@app.route('/')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    s = "SELECT * FROM student"
    cur.execute(s)
    rows = cur.fetchall()
    print(rows)

    return rows[0]



if __name__ == '__main__':
    app.run(debug=True)
