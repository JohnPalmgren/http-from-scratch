import threading
import time
import pytest 
from lib.http_server import HTTPServer 

@pytest.fixture
def running_server():
    """
    Fixture to set up and run the HTTPServer in a daemon thread.
    Yields the port the server is running on.
    """
    # TODO Find and allocate free port
    PORT = 8000
    server = HTTPServer(host='localhost', port=PORT)
    
    # Run the server in a daemon thread so it exits with the test
    server_thread = threading.Thread(target=server.run_server, daemon=True)
    server_thread.start()
    
    # Give the server a moment to start up
    time.sleep(0.1)

    yield PORT