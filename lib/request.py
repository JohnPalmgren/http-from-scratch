class Request():

    def handle_request(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            print(f'Received request {request.split()[1]}')
        else:
            print('Request empty')

        response = """HTTP/1.1 200 OK
            Content-Type: text/html

            <html>
            <body>
            <h1>Hello world</h1>
            </body>
            </html>
        """
        client_socket.send(response.encode('utf-8'))
        client_socket.close()