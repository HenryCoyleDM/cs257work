from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import random
import psycopg2

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
        special = request.form["special"]
        print(f"Recieved POST request: {low} to {high}")
    else:
        # adapted from https://pythonbasics.org/flask-tutorial-routes/
        low = request.args.get("low")
        high = request.args.get("high")
        special = request.args.get("special")
        print(f"Recieved GET request. Arguments are {request.args}")
    if special == "city":
        random_city = get_random_city_by_population()
        return f"{random_city[0]}, {random_city[1]}"
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

# gets a random US city from the database, weighted by population
def get_random_city_by_population():
    # adapted from sample code by Matthew Lepinski
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "coyleh2",
        user = "coyleh2",
        password = "books257beach"
    )
    if connection is None:
        print("Connection failed")
    cursor = connection.cursor()
    # adapted from https://learnsql.com/cookbook/how-to-sum-values-of-a-column-in-sql/
    cursor.execute("SELECT SUM(city_population) AS total_population FROM us_cities")
    total_population = cursor.fetchone()
    cursor.execute("SELECT * FROM us_cities ORDER BY city_population DESC")
    all_cities = cursor.fetchall()
    random_resident = random.randint(1, total_population)
    for city in all_cities:
        random_resident -= city[2]
        if random_resident <= 0:
            return city
    return None

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)
