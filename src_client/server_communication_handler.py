"""
server_communication_handler.py
"""
import logging
import requests
from signal_interpreter_client.src_client.exceptions import ClientError

logger = logging.getLogger(__name__)


def message_post(url_addr, message):
    """
    message_post method
    """
    message_header = {"content-type": "application/json"}
    try:
        response = requests.post(url_addr, json=message, headers=message_header)
        logger.info("Successfully sending POST msg. Response %s", response)
        return response
    except requests.exceptions.Timeout as err:
        logger.exception("Timeout error %s", err)
    except requests.exceptions.ConnectionError as err:
        logger.exception("Connection error %s", err)
    except Exception as err:
        raise ClientError(f"Client error while sending POST message with json: {message}") from err
