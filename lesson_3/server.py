import socket
import sys
import json
from lesson_3.comon.variables import action, account_name, response, max_connections, presence, time, user, error, \
    default_port
from lesson_3.comon.utils import get_message, send_message


def process_client_message(message):
    if action in message and message[action] == presence and time in message and user in message and \
            message[user][account_name] == 'Guest':
        return {response: 200}
    return {
        response: 400,
        error: 'Bad Request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = default_port
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('After the -"p" parameter you must enter the port number')
        sys.exit(1)
    except ValueError:
        print('Enter port in range 1024 - 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('After the parameter "a"- you must enter the address that the server ll listen')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(max_connections)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response_server = process_client_message(message_from_client)
            send_message(client, response_server)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Received an incorrect message from the client')
            client.close()


if __name__ == '__main__':
    main()