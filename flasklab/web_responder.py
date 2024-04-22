# sample code from Matthew Lepinski

import flask
import psycopg2

app = flask.Flask(__name__)

@app.route('/add/<number1>/<number2>')
def get_sum(number1, number2):
    try:
        num1 = int(number1)
        num2 = int(number2)
        return str(num1 + num2)
    except ValueError:
        return '<p style="color:Red">Please input 2 integers</p>'

@app.route('/pop/<abbreviation>')
def get_state_population(abbreviation):
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "coyleh2",
        user = "coyleh2",
        password = "books257beach"
    )
    if connection is None:
        print("Connection failed")
        return '<p style="color:Red">Failed to connect to database</p>'
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM us_states WHERE code LIKE '%s'" % abbreviation)
    row = cursor.fetchone()
    if row is None:
        return '<p style="color:Red">Please enter a valid state abbreviation</p>'
    else:
        return row[0]

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port=my_port) 