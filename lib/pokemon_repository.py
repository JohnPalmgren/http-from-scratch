from lib.pokemon import Pokemon

class PokemonRepository():
    def __init__(self, connection):
        self.connection = connection

    def add(self, pokemon):
        command = 'INSERT INTO pokemons (name, type) VALUES (%s, %s)'
        self.connection.execute(command, [pokemon.name, pokemon.class_type])
    
    def all(self):
        command = 'SELECT * FROM pokemons'
        rows = self.connection.execute(command)
        return [Pokemon(row["name"], row["type"]) for row in rows]
