#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

import functions, argparse, random, socket, sys, re, threading
from threading import Thread

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))

    print('Listening at', sock.getsockname())
    message = ''

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        command = text.split(' ')

        if command[0] == "blah":
            message = ""
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "logIn":
            message = functions.logIn(command,address)
            sock.sendto(message.encode('ascii'), address)
            
        elif command[0] == "whoIsOn":
            message = functions.whoIsOn()
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "send":
            message = functions.sendMess(command,address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "logOut":
            message = functions.logOut(command,address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "help":
            message = functions.help()
            sock.sendto(message.encode('ascii'), address)

        else:
            message =">> Command not recognized"
            sock.sendto(message.encode('ascii'), address)
       

    print('The client at {} says {!r}'.format(address, text))
    sock.sendto(message.encode('ascii'), address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))

    delay = 0.1 # seconds
    text = 'blah'
    data = text.encode('ascii')

    functions.menu()
  
    while True:
        sock.send(data)
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout as exc:
            if delay > 2.0:
                raise RuntimeError('I think the server is down') from exc
        else:
            print(data.decode('ascii'))
            break # we are done, and can stop looping

    while True:
        print("> ", end="")
        text = input()
        data = text.encode('ascii')

        sock.send(data)
        sock.settimeout(delay)

        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout as exc:
            delay *= 2  # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('I think the server is down') from exc
        else:
            response = data.decode('ascii')
            print(response)
            if response == 'logOut':
                break

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                     ' pretending packets are often dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)


