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
    split = row.split()
    print("Northfield is at Latitude: %s, Longitude: %s", split[3], split[4])