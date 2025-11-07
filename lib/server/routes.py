from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

class Routes:
    def __init__(self, req):
        self._req = req
        self._path = req.split()[1]
        self.repo = PokemonRepository()

    def get(self):
        match self._path:
            case "/":
                file_name = "templates/home/index.html"
            case "/pokemon":
                file_name = "templates/pokemon/index.html"
            case "/pokemon/add":
                file_name = "templates/pokemon/new.html"
            case "/pokemon/data":
                header = "HTTP/1.1 200 OK\r\nContent-Type: json\r\n\r\n"
                return header + self.repo.get_json()
            case _:
                return self._page_not_found()

        return self._generate_response(file_name)
    
    def post(self):
        raw_form_data = self._req.split("\r\n\r\n")[1]
        form_data = self._process_form_data(raw_form_data)
        redirect = False
        match self._path:
            case "/pokemon":
                name = form_data["name"]
                type = form_data["type"]
                pokemon = Pokemon(name, type)
                self.repo.add(pokemon)
            case _:
                return self._page_not_found()
        if redirect:
            self._path = redirect
        return self.get()



    def _page_not_found(self):
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        file_name = "templates/errors/not_found.html"
        try:
            with open(file_name, "r") as file:
                html_body = file.read()

            response = header + html_body
            return response

        except FileNotFoundError:
            header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
            return header
        
    def _generate_response(self, file_name):
        try:
            with open(file_name, "r") as file:
                html_body = file.read()

            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

            response = header + html_body
            return response

        except FileNotFoundError:
            return self._page_not_found()
        
    def _process_form_data(self, raw_form_data):
        formatted_data = {}
        key_value_strings = raw_form_data.split("&")
        for key_val in key_value_strings:
            key = key_val.split("=")[0]
            value = key_val.split("=")[1]
            formatted_data[key] = value
        return formatted_data
