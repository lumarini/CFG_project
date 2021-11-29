CREATE DATABASE movie_recommendations;

USE movie_recommendations; 

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(55),
    email VARCHAR(55),
	password VARCHAR(20),
    PRIMARY KEY (id)
);

INSERT INTO users (username, email, password)
VALUES 
('lumarini', 'lumarini@ust', 'my_password'),
('user', 'user@email', 'user_password');

SELECT * from users;

drop table users;

