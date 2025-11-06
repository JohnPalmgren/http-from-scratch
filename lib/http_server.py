import socket
import threading

class HTTPServer():
    def __init__(self, host='localhost', port=8000):
        self._host = host
        self._port = port

    def __create_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((self._host, self._port))
        server_socket.listen(5)

        print(f'Server running on http://{self._host}:self.{self._port}')

        return server_socket
    
    def __handle_request(self, client_socket):
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

    def run_server(self):
        server = self.__create_server()
        try:
            while True:
                client_socket, address = server.accept()
                print(f'New connection from {address}')
                # self.__handle_request(client_socket)
                thread = threading.Thread(
                    target=self.__handle_request, 
                    args=(client_socket,)
                )
                thread.start()
        except KeyboardInterrupt:
            server.close()