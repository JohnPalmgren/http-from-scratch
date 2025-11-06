from lib.request import Request

def test_get_with_valid_input(mocker):
    mock_soc = mocker.Mock()
    mock_soc.recv.return_value = b'GET / HTTP/1.1'
    req = Request()
    req.handle_request(mock_soc)
    args, _ = mock_soc.send.call_args
    sent_data_str = args[0] .decode('utf-8')
    first_line = sent_data_str.splitlines()[0]
    assert "200 OK" in first_line
    mock_soc.recv.assert_called_once_with(1024)
    mock_soc.close.assert_called_once()