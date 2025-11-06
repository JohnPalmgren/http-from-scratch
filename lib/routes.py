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
                return "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"

        try:
            with open(file_name, "r") as file:
                html_body = file.read()

            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

            response = header + html_body
            return response

        except FileNotFoundError:
            print("Error file not found")
            # TODO implement generic 404
            header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
            return header
