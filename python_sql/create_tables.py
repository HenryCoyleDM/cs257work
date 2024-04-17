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
cursor.execute("DROP TABLE IF EXISTS us_cities CASCADE")
cursor.execute("CREATE TABLE us_cities (city_name TEXT, state_name TEXT, city_population INTEGER, latitude FLOAT, longitude FLOAT);")
cursor.execute("DROP TABLE IF EXISTS us_states CASCADE")
cursor.execute("CREATE TABLE us_states (code VARCHAR(2), state_name2 TEXT, state_population INTEGER);")
connection.commit()