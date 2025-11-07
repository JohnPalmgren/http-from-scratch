from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

# TODO replace with mock
def test_added_pokemon_stored_in_store():
    bbs = Pokemon("Bulbasaur", "grass")
    ev = Pokemon("eevee", "normal")
    repo = PokemonRepository()
    repo.add(bbs)
    repo.add(ev)
    assert repo.store == [
        Pokemon("Bulbasaur", "grass"), 
        Pokemon("eevee", "normal")
    ]

def test_pokemon_json():
    bbs = Pokemon("Bulbasaur", "grass")
    ev = Pokemon("eevee", "normal")
    repo = PokemonRepository()
    repo.add(bbs)
    repo.add(ev)
    json = repo.get_json()
    assert json == '[{"name": "Bulbasaur", "class_type": "grass"}, {"name": "eevee", "class_type": "normal"}]'