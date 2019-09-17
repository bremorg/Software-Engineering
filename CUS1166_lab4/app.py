#from flask import Flask, render_template
from flask import Flask, render_template
app = Flask(__name__)

fruits = ("apples", "bananas", "grapes")

students = []
students.append(("Fred", "Senior", 84))
students.append(("Mary", "Senior", 92))
students.append(("John", "Freshmen", 76))
students.append(("Steve", "Junior", 88))
students.append(("Mark", "Freshmen", 82))
students.append(("Jill", "Sophomore", 72))
students.append(("Bob", "Senior", 64))


@app.route("/")
def index():
	#return "<p>Hi</p>"
	return render_template('index.html') 

@app.route("/welcome/<string:name>")
def welcome(name):
	return render_template('welcome.html', name=name)

@app.route("/roster/<int:view>")
def roster(view):
	return render_template('roster.html', view=view, student_view=students)

