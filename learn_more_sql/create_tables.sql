DROP TABLE IF EXISTS us_cities_population;
CREATE TABLE us_cities (
    city_name TEXT,
    state_name TEXT,
    city_population INTEGER,
    latitude FLOAT,
    longitude FLOAT
);
DROP TABLE IF EXISTS us_states_population;
CREATE TABLE us_states_population (
    code VARCHAR(2),
    state_name TEXT,
    state_population INTEGER
);