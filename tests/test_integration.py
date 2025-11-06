import socket
import pytest

# Mimic a client sending a request to test server returns expected result
def test_server_response(running_server):
    """Test if the server sends the 'Hello world' response."""
    
    # The 'running_server' argument is automatically filled by pytest
    # with the 'port' value we yielded from the fixture.
    port = running_server
    response = b""
    try:
        # Create a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', port))
        
        # Send a simple HTTP request
        request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client_socket.sendall(request)
        
        # Receive the response
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data
            
        client_socket.close()

    except Exception as e:
        # 'pytest.fail' is the equivalent of 'self.fail'
        pytest.fail(f"Client connection failed: {e}")

    assert b"HTTP/1.1 200 OK" in response