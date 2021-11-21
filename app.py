from flask import Flask, render_template, redirect, request, send_from_directory
import psycopg2
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

select_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':[], 'teacher':['teacher', 'section', 'tutors']}
delete_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':[], 'teacher':['teacher', 'section', 'tutors']}

@app.route('/')
def login_page():
    return render_template('login.html')


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
        return render_template('error.html', Error = "User credentials don't match")


@app.route('/home', methods=['POST'])
def get_table_name():
    return render_template('index.html')


@app.route('/home', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/select', methods=['GET'])
def get_select():
    return render_template('select.html')


@app.route('/select', methods=['POST'])
def select():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        relation = request.form['relation']
        s = "SELECT USER"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in select_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')

        s = "SELECT * FROM " + relation
        cur.execute(s)
        rows = cur.fetchall()
        s = "SELECT column_name FROM information_schema.columns WHERE table_name = '" + relation + "'"
        cur.execute(s)
        heading = cur.fetchall()
        headings = []
        for i in heading:
            headings.append(i[0])
        return render_template('select.html', table = relation, headings = headings, data = rows)

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/delete')
def deletePage():
    return render_template('delete.html')


@app.route('/delete', methods = ['POST'])
def delete():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        relation = request.form['relation']
        s = "SELECT USER"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in delete_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')

        s = "SELECT * FROM " + relation
        cur.execute(s)
        rows = cur.fetchall()
        s = "SELECT column_name FROM information_schema.columns WHERE table_name = '" + relation + "'"
        cur.execute(s)
        heading = cur.fetchall()
        headings = []
        for i in heading:
            headings.append(i[0])
        return render_template('delete.html', table = relation, headings = headings, data = rows)

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/dele', methods=['POST'])
def dele():
    print('yes')


if __name__ == '__main__':
    app.run(debug=True)
