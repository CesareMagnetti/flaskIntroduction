import re
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# instanciate a Flask application, __name__ will reference this file, embedding it in a flask server
app = Flask(__name__)
# where database is configured, using sqlite and everything will be stored in test.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) # pass in app to the database

# class to handle new entries in our agenda database
class Todo(db.Model):
    # task id
    id = db.Column(db.Integer, primary_key=True)
    # content of the task
    content = db.Column(db.String(200), nullable=False) # not be left blank
    # if task was completed
    completed = db.Column(db.Integer, default=0)
    # automatically store the time when the task was created
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # every time we create a new element is going to return the task id
    def __repr__(self):
        return '<task %r>' % self.id

# create route so that when we browse to the URL we dont error 404
# we pass in route() the URL string of where we want to route the app,
# for now we just rout to the main directory
@app.route('/', methods=['POST', 'GET'])
# define function for the abouve route
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)

        # add new entry to the database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'error adding new task'
    else:
        # display all current task in order of date created
        tasks = Todo.query.order_by(Todo.date_created).all()
        # we called the 'templates' folder like that since render_template will look for files in that folder
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'error: problem deleting the task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    # get the current task being updated
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        # update contest of the selected task
        task.content = request.form['content']

        try:
            # commit changes to database
            db.session.commit()
            return redirect('/')
        except:
            return 'error updating task'
    else:
        # we called the 'templates' folder like that since render_template will look for files in that folder
        return render_template('update.html', task=task)



if __name__ == "__main__":
    app.run(debug = True) #remove debug when we are done developing, it will print errors on the web page