import socket
import threading
from lib.request import Request

class HTTPServer():
    def __init__(self, host='localhost', port=8000):
        self._host = host
        self._port = port

    def __create_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((self._host, self._port))
        server_socket.listen(5)

        print(f'Server running on http://{self._host}:{self._port}')

        return server_socket

    def run_server(self):
        server = self.__create_server()
        try:
            while True:
                client_socket, address = server.accept()
                req = Request()
                thread = threading.Thread(
                    target=req.handle_request, 
                    args=(client_socket,)
                )
                thread.start()
        except KeyboardInterrupt:
            server.close()