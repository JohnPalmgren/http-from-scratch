DROP TABLE IF EXISTS pokemons;

CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name text,
    type text
);

INSERT INTO pokemons (name, type) VALUES ('Charizard', 'fire');
INSERT INTO pokemons (name, type) VALUES ('Lucario', 'steel');
INSERT INTO pokemons (name, type) VALUES ('Umbreon', 'dark');
INSERT INTO pokemons (name, type) VALUES ('Pikachu', 'electric');
