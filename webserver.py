"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python3 server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, url_for, flash

from models import Class, Student, Enrollment, db 


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

app.run(host='0.0.0.0', port=8111)

#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of:
#
#     postgresql://USER:PASSWORD@34.75.94.195/proj1part2
#
# For example, if you had username gravano and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://gravano:foobar@34.75.94.195/proj1part2"
#
DATABASEURI = f"postgresql://USER:PASSWORD/project1"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
# engine.execute("""CREATE TABLE IF NOT EXISTS test (
#   id serial,
#   name text
# );""")
#engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
#
# see for routing: https://flask.palletsprojects.com/en/2.0.x/quickstart/?highlight=routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: https://flask.palletsprojects.com/en/2.0.x/api/?highlight=incoming%20request%20data

  """

  # DEBUG: this is debugging code to see what request looks like
  print(request.args)


## OUR WORK


# Studio
@app.route('/studios')
def studios():
    try:
        cursor = g.conn.execute("SELECT * FROM Studio")
        studios = []
        for result in cursor:
            studio_dict = {
                'id': result[0],
                'name': result[1],
                'address': result[2],
                'phone_number': result[3]
            }
            studios.append(studio_dict)
        cursor.close()
        context = dict(studios=studios)
        return render_template("studio.html", **context)
    except Exception as e:
        print(e)
        return render_template('error.html')


# Instructor 
@app.route('/instructors')
def instructors():
    cursor = g.conn.execute("SELECT * FROM instructor")
    instructors = cursor.fetchall()
    cursor.close()
    return render_template("instructors.html", instructors=instructors)

# Registration
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        confirm_email = request.form['confirm_email']
        phone = request.form['phone']
        interests = request.form['interests']

        # Create a new student object and add it to the database
        new_student = Student(name=name, student_id=username, email=email, phone_number=phone, interests=interests)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('registration.html')

# To Enroll Student
# relationship between Studio and Student
@app.route('/enroll', methods=['POST'])
def enroll():
    student_id = request.form.get('student_id')
    class_id = request.form.get('class_id')
    studio_id = request.form.get('studio_id')

    # Get the student and class objects from the database
    student = Student.query.get(student_id)
    class_ = Class.query.get(class_id)

    # Add the enrollment to the database
    enrollment = Enrollment(studio_id=studio_id, student=student, class_=class_)
    db.session.add(enrollment)
    db.session.commit()

    flash('You have successfully enrolled in the class!', 'success')

    return redirect(url_for('class'))

