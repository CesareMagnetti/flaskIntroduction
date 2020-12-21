from flask import Flask

# instanciate a Flask application, __name__ will reference this file, embedding it in a flask server
app = Flask(__name__)

# create route so that when we browse to the URL we dont error 404
# we pass in route() the URL string of where we want to route the app,
# for now we just rout to the main directory
@app.route('/')

# define function for the abouve route
def index():
    return "hello world"
if __name__ == "__main__":
    app.run(debug = True)
