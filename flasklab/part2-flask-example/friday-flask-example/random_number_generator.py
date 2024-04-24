from flask import Flask
from flask import render_template
import random

# sample code from Matthew Lepinski

app = Flask(__name__)

@app.route('/random<arguments>')
def rand(arguments):
    return arguments
    return render_template("random.html", randNum=num, low=low, high=high)

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
