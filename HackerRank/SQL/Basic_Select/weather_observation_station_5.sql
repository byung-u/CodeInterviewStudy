(SELECT CITY,LENGTH(CITY) as min_len FROM STATION ORDER BY min_len, CITY ASC LIMIT 1) 
UNION
(SELECT CITY,LENGTH(CITY) as max_len FROM STATION ORDER BY max_len DESC, CITY ASC LIMIT 1);