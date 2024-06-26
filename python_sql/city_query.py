import psycopg2

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
cursor.execute("SELECT * FROM us_cities WHERE city_name LIKE 'Northfield' AND state_name LIKE 'Minnesota'")
row = cursor.fetchone()
if row is None:
    print("Northfield is not present in the database")
else:
    print("Northfield is at Latitude: %f, Longitude: %f" % (row[3], row[4]))
cursor.execute("SELECT * FROM us_cities ORDER BY city_population DESC")
row = cursor.fetchone()
print("%s has the largest population: %d" % (row[0], row[2]))
cursor.execute("SELECT * FROM us_cities WHERE state_name LIKE 'Minnesota' ORDER BY city_population ASC")
row = cursor.fetchone()
print("%s is the Minnesota city with the least population: %d" % (row[0], row[2]))
cursor.execute("SELECT * FROM us_cities ORDER BY latitude ASC")
row = cursor.fetchone()
southernmost = "%s, %s" % (row[0], row[1])
cursor.execute("SELECT * FROM us_cities ORDER BY latitude DESC")
row = cursor.fetchone()
northernmost = "%s, %s" % (row[0], row[1])
cursor.execute("SELECT * FROM us_cities ORDER BY longitude ASC")
row = cursor.fetchone()
westernmost = "%s, %s" % (row[0], row[1])
cursor.execute("SELECT * FROM us_cities ORDER BY longitude DESC")
row = cursor.fetchone()
easternmost = "%s, %s" % (row[0], row[1])
print("The furthest cities in the cardinal directions are: North: %s; East: %s; South: %s; West: %s" % (northernmost, easternmost, southernmost, westernmost))
state_input = input("Enter a state name or abbreviation: ")
# adapted from https://learnsql.com/cookbook/how-to-sum-values-of-a-column-in-sql/
cursor.execute("SELECT SUM(city_population) AS total_population FROM us_cities WHERE state_name LIKE %s", [state_input])
row = cursor.fetchone()
if row is not None and row[0] is not None:
    total_population = row[0]
    print("The total population of cities in %s is %d" % (state_input, total_population))
else:
    cursor.execute("SELECT state_name2 FROM us_states WHERE code = %s", [state_input])
    row = cursor.fetchone()
    if row is None:
        print("Please enter a valid state name or code")
    else:
        state_name = row[0]
        cursor.execute("SELECT SUM(city_population) AS total_population FROM us_cities WHERE state_name LIKE %s", [state_name])
        row = cursor.fetchone()
        if row is not None and row[0] is not None:
            total_population = row[0]
            print("The total population of cities in %s (%s) is %d" % (state_name, state_input, total_population))
        else:
            print("Please enter a valid state name or code")
