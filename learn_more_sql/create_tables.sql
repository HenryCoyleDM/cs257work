DROP TABLE IF EXISTS us_cities CASCADE;
CREATE TABLE us_cities (
    city_name TEXT,
    state_name TEXT,
    city_population INTEGER,
    latitude FLOAT,
    longitude FLOAT
);
DROP TABLE IF EXISTS us_states CASCADE;
CREATE TABLE us_states (
    code VARCHAR(2),
    state_name2 TEXT,
    state_population INTEGER
);
