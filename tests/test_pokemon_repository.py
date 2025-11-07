from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

def test_pokemon_all(db_connection):
    db_connection.seed("seeds/pokemon.sql")
    repo = PokemonRepository(db_connection)
    pokemons = repo.all()
    assert pokemons == [
        Pokemon('Charizard', 'fire'),
        Pokemon('Lucario', 'steel'),
        Pokemon('Umbreon', 'dark'),
        Pokemon('Pikachu', 'electric'),
    ]

def test_pokemon_add(db_connection):
    db_connection.seed("seeds/pokemon.sql")
    bbs = Pokemon("Bulbasaur", "grass")
    ev = Pokemon("eevee", "normal")
    repo = PokemonRepository(db_connection)
    repo.add(bbs)
    repo.add(ev)
    pokemons = repo.all()
    assert pokemons == [
        Pokemon('Charizard', 'fire'),
        Pokemon('Lucario', 'steel'),
        Pokemon('Umbreon', 'dark'),
        Pokemon('Pikachu', 'electric'),
        Pokemon("Bulbasaur", "grass"), 
        Pokemon("eevee", "normal")
    ]