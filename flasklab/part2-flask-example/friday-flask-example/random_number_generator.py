from flask import Flask
from flask import render_template
import random

# sample code from Matthew Lepinski

app = Flask(__name__)

@app.route('/random')
def index():
    return render_template("index.html")

@app.route('/random/<low>/<high>')
def random(low, high):
    return "a random number from %s to %s" % (low, high)
    return render_template("random.html", randNum=num, low=low, high=high)

@app.route('/random/<arguments>')
def single_argument(argument):
    return argument

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
