from lib.server.http_server import HTTPServer

def test_server_initiates_with_host_and_port():
    server = HTTPServer('localhost', 8080)
    assert server._host == 'localhost'
    assert server._port == 8080
