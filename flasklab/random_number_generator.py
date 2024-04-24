from flask import Flask
from flask import render_template
from flask import request
import random

# sample code from Matthew Lepinski

app = Flask(__name__)

# adapted from https://pythonbasics.org/flask-tutorial-routes/
@app.route('/random', methods=["POST", "GET"])
def generate_random_number():
    # if argument_low is not None and argument_high is not None:
        # return "low: %s, high: %s" % (argument_low, argument_high)
    # else:
        # return render_template("index.html")
    if request.method == "POST":
        low = request.form["low"]
        high = request.form["high"]
        return "low: %s, high: %s" % (low, high)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
