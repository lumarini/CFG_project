CREATE DATABASE movie_recommendations;

USE movie_recommendations; 

CREATE TABLE users (
	user_id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(60),
	password BLOB,
    PRIMARY KEY (user_id)
);

CREATE TABLE movies (
    movie_id INT,
	movie_name VARCHAR(60),
    movie_detail VARCHAR(10000),
    movie_poster_path VARCHAR(1000),
    PRIMARY KEY (movie_id)
);

CREATE TABLE movies_watched (
	mw_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT, 
    user_id INT,
    PRIMARY KEY (mw_id)
);


-- ############################################################


-- Run full code up to  the line above. The next line are only example queries I left as it is useful to fetch data as needed, 
-- or to drop tables after they are too full of tests run on it.


-- #############################################################



-- SELECT * from users;

-- SELECT u.user_id, u.username, m.movie_id, m.movie_name
-- FROM users u, movies m, movies_watched mw
-- WHERE mw.user_id = u.user_id AND mw.movie_id = m.movie_id 
-- AND u.user_id = 1; 

-- SELECT u.user_id, u.username, u.password
-- FROM users as u
-- WHERE username = 'lumarini';

-- drop table users; 
-- drop table movies; 
-- drop table movies_watched; 