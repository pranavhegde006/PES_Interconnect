from flask import Flask, render_template, redirect, request, send_from_directory
import psycopg2
import psycopg2.extras
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


select_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'admin':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':['department', 'section', 'course'], 'teacher':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors']}
delete_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'admin':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':[], 'teacher':[]}
insert_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'admin':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':[], 'teacher':[]}
update_perms = {'postgres':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'admin':['club', 'consists', 'course', 'department', 'managed_by', 'offers', 'opts', 'section', 'staff', 'student', 'teacher', 'teaches', 'tutors'], 'student':[], 'teacher':[]}


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
        size = len(rows)
        for i in heading:
            headings.append(i[0])
        return render_template('delete.html', table = relation, headings = headings, data = rows, length = size)

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/dele', methods=['POST'])
def dele():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        id = request.get_json()
        s = "SELECT * FROM consists"
        cur.execute(s)
        rows = cur.fetchall()
        # print(type(rows))
        c_id = rows[int(id['ids'])][0]
        srn = rows[int(id['ids'])][1]
        s = "BEGIN"
        cur.execute(s)
        s = "DELETE FROM consists WHERE club_id = " + str(c_id) + " AND srn = " + str(srn)
        cur.execute(s)
        s = "COMMIT"
        cur.execute(s)
        return render_template('delete.html', status = "Entry deleted SUCCESSFULLY!")
    except Exception as E:
        return render_template('error.html', Error = str(E))


@app.route('/insert')
def insert_page():
    return render_template('insert.html')


@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        c_id = request.form['c_id']
        name = request.form['name']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        relation = 'club'
        s = "SELECT USER"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in select_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')
        s = "BEGIN"
        cur.execute(s)
        s = "INSERT INTO club VALUES(" + str(c_id) + ", '" + str(name) + "')"
        cur.execute(s)
        s = "COMMIT"
        cur.execute(s)
        print(c_id, name)
        return render_template('insert.html')
    except Exception as E:
        return render_template('error.html', Error = str(E))
    

@app.route('/update')
def get_cgpa():
    return render_template('update.html')


@app.route('/get_cgpa', methods=["POST"])
def show_cgpa():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        srn = request.form['srn']
        s = "BEGIN"
        cur.execute(s)
        s = "SELECT USER"
        relation = "student"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in update_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')

        s = "SELECT srn, name, cgpa FROM student where srn = " + str(srn)
        cur.execute(s)
        rows = cur.fetchall()
        # s = "SELECT column_name FROM information_schema.columns WHERE table_name = '" + relation + "'"
        # cur.execute(s)
        # heading = cur.fetchall()
        headings = ['srn', 'name', 'cgpa']
        # for i in heading:
            # headings.append(i[0])
        s = "COMMIT"
        cur.execute(s)
        return render_template('update.html', table = relation, headings = headings, data = rows)

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/update_cgpa', methods=["POST"])
def update_cgpa():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        srn = request.form['srn']
        s = "BEGIN"
        cur.execute(s)
        s = "SELECT USER"
        relation = "student"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in update_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')
        new_cgpa = request.form['new_cgpa']
        srn = request.form['srn']
        s = "UPDATE student SET cgpa = " + str(new_cgpa) + " where srn = " + str(srn)
        cur.execute(s)
        s = "COMMIT"
        cur.execute(s)
        return render_template('update.html', table = "UPDATED SUCCESSFULLY!")

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/get_top_students', methods=['POST'])
def get_top_students():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        percent = request.form['percent']
        s = "BEGIN"
        cur.execute(s)
        s = "SELECT USER"
        relation = "student"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in select_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')
        s = "select srn,name,cgpa from student order by cgpa desc fetch first ( select count(*) * " + percent + "/100 from student ) rows only"
        cur.execute(s)
        rows = cur.fetchall()
        s = "COMMIT"
        cur.execute(s)
        return render_template('home.html', table = "Top " + str(percent) + "% of students", data=rows, headings = ['srn', 'name', 'cgpa'])

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/no_course_teachers', methods = ["POST"])
def no_course_teachers():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        s = "BEGIN"
        cur.execute(s)
        s = "SELECT USER"
        relation = "teacher"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in select_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')
        s = "select employee_id, name , email_id from teacher as u where not exists (select * from teaches as t where t.employee_id=u.employee_id)"
        cur.execute(s)
        rows = cur.fetchall()
        s = "COMMIT"
        cur.execute(s)
        return render_template('home.html', table = "Teachers who are currently not teaching any course", data=rows, headings = ['Employee ID', 'Name', 'Email ID'])

    except Exception as e:
        return render_template('error.html', Error = str(e))


@app.route('/teachers_dept', methods=["POST"])
def get_teachers():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        s = "BEGIN"
        cur.execute(s)
        s = "SELECT USER"
        relation = "teacher"
        cur.execute(s)
        rows = cur.fetchall()
        cur_user = rows[0]['user']
        if(relation not in select_perms[cur_user]):
            return render_template('error.html', Error = 'Unauthorized access')
        dept = request.form['dept']
        s = "select name , phone_no,email_id from teacher where employee_id in (select employee_id from teaches where dept_id in (select dept_id from department where name='" + dept + "'))"
        cur.execute(s)
        rows = cur.fetchall()
        s = "COMMIT"
        cur.execute(s)
        return render_template('home.html', table = "Teachers who are currently not teaching any course", data=rows, headings = ['Name', 'Phone No', 'Email ID'])

    except Exception as e:
        return render_template('error.html', Error = str(e))



if __name__ == '__main__':
    app.run(debug=True)
