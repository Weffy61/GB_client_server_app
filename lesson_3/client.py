import sys
import json
import socket
import time
from comon.variables import action, presence, time, user, account_name, response, error
from comon.variables import default_ip_address, default_port
from comon.utils import get_message, send_message


def create_presence(account_name='Guest'):
    out = {
        action: presence,
        time: time.time(),
        user: {
            account_name: account_name
        }
    }
    return out


def process_answer(message):
    if response in message:
        if message[response] == 200:
            return '200 : OK'
        return f'400 : {message[error]}'
    raise ValueError


def main():
    try:
        server_address = sys.argv[2]
        server_port = int(sys.argv[3])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = default_ip_address
        server_port = default_port
    except ValueError:
        print('Select port in range 1024 - 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    try:
        answer = process_answer(get_message(transport))
        print(answer)
    except(ValueError, json.JSONDecodeError):
        print('Error decoding a message from the server')


if __name__ == '__main__':
    main()

