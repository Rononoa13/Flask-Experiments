CREATE TABLE users (
uid SERIAL PRIMARY KEY,
firstname VARCHAR(100) NOT NULL,
lastname VARCHAR(100) NOT NULL,
email VARCHAR(120) NOT NULL UNIQUE,
pwdhash VARCHAR(100) NOT NULL 
);


INSERT INTO users (firstname, lastname, email, pwhash) VALUES ('Lalith', 'Polepeddi', 'lalith@example.com', 'learning-flask');
