-- counts the number of earthquakes that occurred below 200km of depth
SELECT COUNT(*) FROM earthquakes WHERE quakedepth>200;
-- lists the earthquakes with magnitude at least 5 that occurred in the US network
SELECT FROM earthquakes WHERE magnitude>5 AND net LIKE 'us';
-- counts the number of earthquakes that occurred near Indonesia (have "Indonesia" in their place description)
SELECT COUNT(*) FROM earthquakes WHERE place LIKE '%Indonesia%';
