import json

class PokemonRepository():
    def __init__(self):
        self.store = []

    def add(self, pokemon):
        self.store.append(pokemon)

    def get_json(self):
        json_list = []
        for pokemon in self.store:
            pokemon_object = {"name": pokemon.name, "class_type": pokemon.class_type}
            json_list.append(json.dumps(pokemon_object))
        return json_list
