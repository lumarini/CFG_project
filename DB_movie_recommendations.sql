CREATE DATABASE movie_recommendations;

USE movie_recommendations; 

CREATE TABLE users (
	user_id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(55),
    email VARCHAR(55),
	password VARCHAR(20),
    PRIMARY KEY (user_id)
);

CREATE TABLE movies (
    movie_id INT,
	movie_name VARCHAR(55),
    movie_detail VARCHAR(55),
    PRIMARY KEY (movie_id)
);

CREATE TABLE movies_watched (
	mw_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT, 
    user_id INT,
    PRIMARY KEY (mw_id)
);

INSERT INTO users (username, email, password)
VALUES 
('lumarini', 'lumarini@ust', 'my_password'),
('enrico', 'enrico@email', 'password'),
('ninamarini', 'nina@email', 'passw'),
('user', 'user@email', 'user_password');


INSERT INTO movies (movie_id, movie_name, movie_detail)
VALUES
(001, 'The Lion King', 'Comedy, Cartoon, Disney'),
(002, 'Monsters, INC.', 'Comedy, Cartoon'),
(003, 'Erin Brokovich', 'Drama'),
(004, 'Bridget Jones Diary', 'Comedy'),
(005, 'Thor', 'Action, Sci-Fi'),
(006, 'Ratatouille', 'Comedy, Cartoon');

INSERT INTO movies_watched (user_id, movie_id)
VALUES 
(1, 001),
(1, 002),
(2, 003),
(2, 004),
(3, 005),
(3, 006);


SELECT * from users;


SELECT u.user_id, u.username, m.movie_id, m.movie_name
from users u, movies m, movies_watched mw
where mw.user_id = u.user_id AND mw.movie_id = m.movie_id;

-- AND u.user_id = 1; 


-- drop table users; 
-- drop table movies; 
-- drop table movies_watched; 