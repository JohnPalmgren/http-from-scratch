from lib.routes import Routes

def test_route_initialised_with_request():
    request = "GET / HTTP/1.1"
    routes = Routes(request)
    assert routes.req == request

def test_valid_get_for_root():
    request = "GET / HTTP/1.1"
    routes = Routes(request)
    res = routes.get()
    success_header = "HTTP/1.1 200 OK"
    assert success_header in res

def test_non_valid_get():
    request = "GET /non-existent-resource HTTP/1.1"
    routes = Routes(request)
    res = routes.get()
    fail_header = "HTTP/1.1 404 Not Found"
    assert fail_header in res

def test_get_for_page():
    request = "GET /pokemon HTTP/1.1"
    routes = Routes(request)
    res = routes.get()
    success_header = "HTTP/1.1 200 OK"
    assert success_header in res