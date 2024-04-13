CREATE VIEW cities_plus_states_populations AS SELECT * FROM us_cities JOIN us_states ON us_cities.state_name = us_states.state_name2;
CREATE VIEW real_populations AS SELECT city_name, state_name, CAST(city_population AS REAL) AS real_city_population, CAST(state_population AS REAL) AS real_state_population FROM cities_plus_states_populations;
CREATE VIEW population_quotients AS SELECT city_name, (real_city_population / real_state_population) AS quotient FROM real_populations;
SELECT * FROM population_quotients ORDER BY quotient DESC;
