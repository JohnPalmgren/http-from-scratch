import socket
import threading

def http_server(host='localhost', port=8000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(host, port)
    server_socket.listen(5)

    print(f'Server running on http://{host}:{port}')

    return server_socket

def handle_request(client_socket):
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