import os

class Request():

    def get(self, request):
        if request.split()[1] == "/":
            file_name = "templates/home/index.html"
            try:
                with open(file_name, "r") as file:
                    html_body = file.read()

                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

                response = header + html_body
                return response

            except FileNotFoundError:
                print("Error file not found")
                # TODO implement generic 404
        
        else: 
            # TODO implement generic 404
            return ""


    def handle_request(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            print(f'Received request {request.split()[1]}')
        else:
            print('Request empty')
        if request.split()[0] == "GET":
            response = self.get(request)

        else:
            response = ""

        client_socket.send(response.encode('utf-8'))
        client_socket.close()