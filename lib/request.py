from lib.routes import Routes

class Request():

    @staticmethod
    def handle_request(client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            routes = Routes(request)
            if request.split()[0] == "GET":
                response = routes.get()
            else:
                response = ""

            client_socket.send(response.encode('utf-8'))
            client_socket.close()
            print(f'Received request {request.split()[1]}')
        else:
            client_socket.close()