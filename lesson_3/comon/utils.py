import json
from lesson_3.comon.variables import max_package_len, encoding


def get_message(client):
    encoded_response = client.recv(max_package_len)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(encoding)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(socket, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(encoding)
    socket.send(encoded_message)
