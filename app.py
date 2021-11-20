from flask import Flask, render_template, redirect, request, send_from_directory
import psycopg2
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    try: 
        DB_HOST = "localhost"
        DB_NAME = "pes_interconnect2"
        DB_USER = request.form['username']
        DB_PASSWORD = request.form['password']
        global conn
        conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST)
        return redirect('/home')
    except:
        return render_template('error.html')



@app.route('/home', methods=['GET'])
def index():
    # try:
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    s = "SELECT * FROM student"
    cur.execute(s)
    rows = cur.fetchall()

    return rows[0]



if __name__ == '__main__':
    app.run(debug=True)
