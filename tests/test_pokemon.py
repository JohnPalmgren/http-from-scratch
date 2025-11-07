from lib.pokemon import Pokemon

def test_pokemon_initiates():
    bulbasaur = Pokemon("Bulbasaur", "grass")
    assert bulbasaur.name == "Bulbasaur"
    assert bulbasaur.class_type == "grass"