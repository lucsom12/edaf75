PRAGMA foreign_keys=OFF;
DROP TABLE IF EXISTS theaters;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS performances;
PRAGMA foreign_keys=ON;

CREATE TABLE theaters (
  theater TEXT,
  capacity INT,
  PRIMARY KEY (theater)
);

CREATE TABLE movies (
  imdbKey TEXT,
  title TEXT,
  year INT,
  PRIMARY KEY (imdbKey)
);

CREATE TABLE ticket (
  screeningID INT,
  ticket_ID INT DEFAULT (lower(hex(randomblob(16)))),
  username TEXT,
  PRIMARY KEY (ticket_ID),
  FOREIGN KEY (screeningID) REFERENCES time_slot(screeningID),
  FOREIGN KEY (username) REFERENCES customer(username)
);

CREATE TABLE users (
  username TEXT,
  fullName TEXT,
  pwd TEXT,
  PRIMARY KEY (username)
);

CREATE TABLE performances (
  imdbKey TEXT,
  theater TEXT,
  date DATE,
  time TIME,
  screeningID INT DEFAULT (lower(hex(randomblob(16)))),
  PRIMARY KEY (screeningID),
  FOREIGN KEY (imdbKey) REFERENCES movies(imdbKey),
  FOREIGN KEY (theater) REFERENCES theaters(theater)
);