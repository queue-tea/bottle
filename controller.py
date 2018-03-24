import sqlite3
import datetime
from bottle import route, run, debug, template, request, static_file, error, redirect, get

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

@get("/images/<filepath:re:.*\.jpg>")
def images(filepath):
    return static_file(filepath, root="images")

@route('/index')
def home():
    return template('templates/index.tpl')

@route('/list')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo ORDER BY posted ASC")
    result = c.fetchall()
    c.close()

    output = template('templates/make_table', rows=result)
    return output

@route('/showcompleted')
def filter_complete():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('templates/make_table', rows=result)
    return output

@route('/showtodo')
def filter_todo():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo WHERE status LIKE '0'")
    result = c.fetchall()
    c.close()
    output = template('templates/make_table', rows=result)
    return output

@route('/sortposted')
def sort_posted():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo ORDER BY posted ASC")
    result = c.fetchall()
    c.close()
    output = template('templates/make_table', rows=result)
    return output

@route('/sortdue')
def sort_due():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo ORDER BY due ASC")
    result = c.fetchall()
    c.close()
    output = template('templates/make_table', rows=result)
    return output

@route('/sortupdated')
def sort_updated():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, description, posted, due, updated, status FROM todo ORDER BY due ASC")
    result = c.fetchall()
    c.close()
    output = template('templates/make_table', rows=result)
    return output

@route('/new', method='GET')
def new_item():
    if request.GET.save:
        task = request.GET.get("task", "").strip()
        description = request.GET.get("description", "").strip()
        due = request.GET.get("due", "").strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        posted = datetime.date.today()
        updated = datetime.date.today()
        c.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES (?,?,?,?,?,?)", (task, description, posted, due, updated, 0))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        redirect("/list")
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id


    else:
        return template('templates/new_task.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:
        task = request.GET.task.strip()
        description = request.GET.description.strip()
        due = request.GET.due.strip()
        status = request.GET.status.strip()

        if status == 'complete':
            status = 1
        else:
            status = 0
        updated = datetime.date.today()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, description = ?, due = ?, updated = ?, status = ? WHERE id LIKE ?", (task, description, due, updated, status, no))
        conn.commit()
        c.close()
        redirect("/list")
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('templates/edit_task', old=cur_data, no=no)

@route('/delete/<no:int>', method='GET')
def delete_item(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id LIKE ?", (str(no)))
    conn.commit()
    c.close()
    redirect("/list")

@route('/item<item:re:[0-9]+>')
def show_item(item):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' % result[0]

@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

debug(True)
run(reloader=True)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment
