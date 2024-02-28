PRAGMA foreign_keys=OFF;
DROP TABLE IF EXISTS theaters;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS time_slot;
PRAGMA foreign_keys=ON;

CREATE TABLE theaters (
  theater_name TEXT,
  capacity INT,
  PRIMARY KEY (theater_name)
);
CREATE TABLE movies (
  names TEXT,
  year INT,
  movie_ID TEXT,
  run_time INT,
  PRIMARY KEY (movie_ID)
);

CREATE TABLE ticket (
  screening_ID INT,
  ticket_ID INT DEFAULT (lower(hex(randomblob(16)))),
  username TEXT,
  PRIMARY KEY (ticket_ID),
  FOREIGN KEY (screening_ID) REFERENCES time_slot(screening_ID),
  FOREIGN KEY (username) REFERENCES customer(username)
);

CREATE TABLE customer (
  username TEXT,
  fullname TEXT,
  pwd TEXT,
  PRIMARY KEY (username)
);

CREATE TABLE time_slot (
  movie_ID TEXT,
  theater_name TEXT,
  start_time TEXT,
  screening_ID INT,
  PRIMARY KEY (screening_ID),
  FOREIGN KEY (movie_ID) REFERENCES movies(movie_ID),
  FOREIGN KEY (theater_name) REFERENCES theaters(theater_name)
);

INSERT 
INTO movies(names, movie_ID, year, run_time)
VALUES ('Shrek3', 'tt001', 2007, 93),
('Shrek2', 'tt002', 2004, 92),
('Shrek1', 'tt003', 2001, 91);

INSERT 
INTO theaters(theater_name, capacity)
VALUES ('Sergelstorg', 1401),
('Bergakungen', 1402),
('Victoria', 1);


INSERT
INTO customer (username,fullname,pwd)
VALUES ('Lucky on da beat', 'Luc Sommerland', 'lucluc12'),
('Joar RR', 'Joar Rinaldo-Roos', 'falcon18'),
('Jeppelito', 'Jesper Lundqvist', '123');

INSERT
INTO time_slot (theater_name, start_time, movie_ID, screening_ID)
VALUES ('Sergelstorg', 'February 04 16:00', 'tt001', 1000),
('Bergakungen', 'February 08 14:15', 'tt002', 2000),
('Victoria', 'February 10 15:00', 'tt003', 3000);

INSERT
INTO ticket (username, screening_ID)
VALUES ('Lucky on da beat', 1000),
('Joar RR',1000),
('Jeppelito',3000);




