CREATE DATABASE testdb;

USE testdb;

CREATE TABLE IF NOT EXISTS users(
	id INT,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

DROP TABLE users;

CREATE TABLE IF NOT EXISTS users(
	id INT,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users(id, name, email, password)
VALUES
	(1, 'musharraf', 'musharaf123@gmail.com', 'mush123'),
    (2, 'ankit', 'ankit123@gmail.com', 'ankit12');
    
TRUNCATE TABLE users;

CREATE TABLE person(
	id INT NOT NULL,
    name VARCHAR(255)
);

INSERT INTO person(id, name)
VALUE(1, 'musharraf');

CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) 
);



CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    CONSTRAINT U_email UNIQUE (email),
    password VARCHAR(255),
);


