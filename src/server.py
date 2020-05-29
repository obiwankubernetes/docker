# script to run our flask app

from flask import Flask

# init flask app
app = Flask(__name__)

# init route
@app.route("/")
def hello():
    return "Hello Kubernetes"