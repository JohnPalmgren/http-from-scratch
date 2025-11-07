import json

class PokemonRepository():
    def __init__(self):
        self.store = []

    def add(self, pokemon):
        self.store.append(pokemon)

    def get_json(self):
        object_list = []
        for pokemon in self.store:
            object_list.append({"name": pokemon.name, "class_type": pokemon.class_type})
        return json.dumps(object_list)
