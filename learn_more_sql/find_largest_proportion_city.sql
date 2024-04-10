DROP TABLE IF EXISTS us_cities_population;
CREATE TABLE us_cities {
    city_name TEXT,
    state_name TEXT,
    city_population INTEGER,
    latitude FLOAT,
    longitude FLOAT
};
COPY us_cities_population FROM 'us-cities-top-1k.csv' DELIMITER ',' CSV;
DROP TABLE IF EXISTS us_states_population;
CREATE TABLE us_states_population {
    code VARCHAR(2),
    state_name TEXT,
    state_population INTEGER
};
COPY us_states_population FROM 'us-state-pop.csv' DELIMITER ',' CSV;
SELECT * FROM us_cities_population JOIN us_states_population ON us_cities_population.state_name == us_states_population.state_name;
