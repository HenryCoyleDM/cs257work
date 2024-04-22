# sample code from Matthew Lepinski

import flask

app = flask.Flask(__name__)

@app.route('/add/<number1>/<number2>')
def my_display(number1, number2):
    try:
        num1 = int(number1)
        num2 = int(number2)
        return str(num1 + num2)
    except ValueError:
        return '<p style="color:Red">Please input 2 integers</p>'


if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port=my_port) 