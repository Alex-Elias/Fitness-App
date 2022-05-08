CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE workout (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    workout_name TEXT,
    description TEXT,
    workout_date date,
    visible INTEGER
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    name TEXT,
    type_id INTEGER REFERENCES types,
    workout_id INTEGER,
    time TEXT,
    distance TEXT,
    date DATE,
    message TEXT,
    visible INTEGER
);

CREATE TABLE prs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    distance TEXT,
    type_id INTEGER REFERENCES types,
    time_h TEXT,
    time_m TEXT,
    time_s TEXT,
    date DATE,
    message TEXT,
    visible INTEGER
);

CREATE TABLE types (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE


);

INSERT INTO types (name) VALUES ('Running');
INSERT INTO types (name) VALUES ('Cycling');
INSERT INTO types (name) VALUES ('Skiing');
INSERT INTO types (name) VALUES ('Swiming');
INSERT INTO types (name) VALUES ('Walking');