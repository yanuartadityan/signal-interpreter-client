import requests

def message_post(url_addr, message):
    message_header = {"Content-Type": "application/json"}
    response = requests.post(url_addr, data={"signal": message}, headers=message_header)
    print(response.text)
