"""
test_server_communication.py
"""
from unittest.mock import patch
from requests.exceptions import Timeout
import pytest

from signal_interpreter_client.src_client.server_communication_handler import message_post


@patch("signal_interpreter_client.src_client.server_communication_handler.requests.post", side_effect=Timeout)
def test_post_with_timeout(mock_post):
    """
    test_post_with_timeout
    """
    with pytest.raises(Timeout):
        message_post("http://127.0.0.1:5000", {"signal": "11"})


@pytest.mark.parametrize("json_input, expected_result", [
    ("11", {"title": "ECU Reset"}),
    ("27", {"title": "Security Access"})
])
def test_post_database(json_input, expected_result):
    """
    test_post_database
    """
    message = {
        "signal": json_input
    }

    s = message_post("http://127.0.0.1:5000", message)
    assert s.json() == expected_result
    
