DROP TABLE IF EXISTS us_cities;
CREATE TABLE us_cities (
    city_name TEXT,
    state_name TEXT,
    city_population INTEGER,
    latitude FLOAT,
    longitude FLOAT
);
DROP TABLE IF EXISTS us_states;
CREATE TABLE us_states (
    code VARCHAR(2),
    name TEXT,
    state_population INTEGER
);
