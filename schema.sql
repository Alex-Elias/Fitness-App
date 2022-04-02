CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE workout (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    workout_name TEXT,
    description TEXT,
    workout_date date,
    visible INTEGER
    );
