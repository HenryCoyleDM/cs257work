from flask import Flask
from flask import render_template
from flask import request
import random

# sample code from Matthew Lepinski

app = Flask(__name__)

# adapted from https://pythonbasics.org/flask-tutorial-routes/
@app.route('/random', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        low = request.form["low"]
        high = request.form["high"]
        return "low: %s, high: %s" % (low, high)
    else:
        return render_template("index.html")

@app.route('/random/<low>/<high>')
def random(low, high):
    return "a random number from %s to %s" % (low, high)
    return render_template("random.html", randNum=num, low=low, high=high)

@app.route('/random/<arguments>')
def single_argument(arguments):
    return arguments

@app.route('/random?<values>')
def form_values(values):
    return "these are values: %s" % (values)

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
