CREATE VIEW cities_plus_states_populations AS SELECT * FROM us_cities JOIN us_states ON us_cities.state_name = us_states.state_name;
SELECT city_name, state_name, CAST(city_population AS REAL) AS real_city_population, CAST(state_population AS REAL) AS real_state_population FROM cities_plus_states_populations;
