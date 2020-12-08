"""
server_communication_handler.py
"""
import requests


def message_post(url_addr, message):
    """
    message_post method
    """
    message_header = {"Content-Type": "application/json"}
    response = requests.post(url_addr, json=message, headers=message_header)
    return response
