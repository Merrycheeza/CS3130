#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network
###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Final Project      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################
#
# this portion of the program handles server and client

import functions, argparse, random, socket, sys, re, threading
from threading import Thread

MAX_BYTES = 65535
host = ('127.0.0.1')
port = 1060

# UDP server function
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print('Listening at', sock.getsockname())
    message = ''

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        command = text.split(' ')
        print('The client at {} says {!r}'.format(address, text))

        if command[0] == "blah":
            message = ""
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "login":
            message = functions.login(command, address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "1":
            message = functions.chooseNext(command, address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "2":
            message = functions.chooseNext(command, address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "quit":
            message = functions.logout(command, address)
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "help":
            message = functions.help()
            sock.sendto(message.encode('ascii'), address)

        elif command[0] == "create":
            message = functions.createAccount(command)
            sock.sendto(message.encode('ascii'), address)

        else:
            message =">> Command not recognized"
            sock.sendto(message.encode('ascii'), address)
       

    print('The client at {} says {!r}'.format(address, text))
    sock.sendto(message.encode('ascii'), address)

# UDP client function
def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))

    delay = 0.1 # seconds
    text = 'blah'
    data = text.encode('ascii')

    functions.titleScreen()

  
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
        print("\n> ", end="")
        text = input()
        data = text.encode('ascii')
        print('\n')

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
            if text == 'quit':
                break

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                     ' pretending packets are often dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
