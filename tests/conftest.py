import threading
import time
import pytest 
import socket
import time
from lib.server.http_server import HTTPServer 
from lib.database_connection import DatabaseConnection

@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

@pytest.fixture
def running_server():
    """
    Fixture to set up and run the HTTPServer in a daemon thread.
    Yields the port the server is running on.
    """
    port = find_free_port()
    host = 'localhost'
    server = HTTPServer(host, port)

    # Run the server in a daemon thread so it exits with the test
    server_thread = threading.Thread(target=server.run_server, daemon=True)
    server_thread.start()

    start_time = time.time()
    timeout = 5
    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError("Server failed to start within 5 seconds")
        try:
            with socket.create_connection((host, port), timeout=0.1):
                break
        except ConnectionRefusedError:
            time.sleep(0.05)

    yield f"http://{host}:{port}"


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind(('localhost', 0)) 
        return soc.getsockname()[1] 