from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
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
    print("Recieved /random request")
    if request.method == "POST":
        low = request.form["low"]
        high = request.form["high"]
        print(f"Recieved POST request: {low} to {high}")
    else:
        # adapted from https://pythonbasics.org/flask-tutorial-routes/
        low = request.args.get("low")
        high = request.args.get("high")
        print(f"Recieved GET request. Arguments are {request.args}")
    if low is None or high is None:
        return render_template("index.html", additional_body="")
    else:
        try:
            random_int = random.randint(int(low), int(high))
            # adapted from https://pythongeeks.org/python-flask-app-routing/#google_vignette
            rerolling_url = url_for("generate_random_number", low=low, high=high)
            return render_template("random.html", random_value=random_int, reroll_bound_url=rerolling_url)
        except ValueError:
            return render_template("index.html", additional_body="Please enter 2 integers")

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
