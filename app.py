from flask import Flask, render_template, url_for

# instanciate a Flask application, __name__ will reference this file, embedding it in a flask server
app = Flask(__name__)

# create route so that when we browse to the URL we dont error 404
# we pass in route() the URL string of where we want to route the app,
# for now we just rout to the main directory
@app.route('/')

# define function for the abouve route
def index():
    # we called the 'templates' folder like that since render_template will look for files in that folder
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True) #remove debug when we are done developing, it will print errors on the web page
