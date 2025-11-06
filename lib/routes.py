class Routes:
    def __init__(self, req):
        self.req = req

    def get(self):
        PATH = self.req.split()[1]
        match PATH:
            case "/":
                file_name = "templates/home/index.html"
            case "/pokemon":
                file_name = "templates/pokemon/index.html"
            case _:
                return self._page_not_found()

        return self._generate_response(file_name)

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