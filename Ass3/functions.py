#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

import argparse, random, sys, re

ONLINE = []
SESSION_ID = []
USERS = ['Larena','Samara','Franco','Janelle']

# function that displays the menu to the client
def menu():
    print("--------------------")
    print("--Welcome to SaMMS--")
    print("--------------------")
    print(">> The following commands are supported:")
    print(">>    logIn <username>")
    print(">>    whoIsOn")
    print(">>    send <username> <message>")
    print(">>    logOut")
    print(">>    help")
    print(">> Remember commands are case sensitive")

# function that handles client logs ins and calls checkMess() to retrieve messages for the user
def logIn(command,address):
    user = command[1]

    if user not in USERS:
        message = "\n>> User "+user+" is not authorized to use SaMMS.\n"

    elif user in ONLINE:
        message = "\n>> Sorry, that user is already logged in.\n"

    else:
        message = checkMess(command)
        record = {'a':user,'b':address[1]}
        ONLINE.append(user)
        SESSION_ID.append(record)
    return message

# function that opens the message database and 
# retrieves the messages for the user it also deletes the ones that have been displayed
# it calls the getMess() protocol to format the messages for the server
def checkMess(command):
    user = command
    data = []
    count = 0
    f = open('messages.txt', 'r')
    mLines = f.readlines()

    for line in mLines:
        line = line.strip()
        tmp = line.split(':')
        uMess = {'a':tmp[0], 'b':tmp[1], 'c':tmp[2]}
        data.append(uMess)
    f.close()

    deliver = []
    
    for i in range(0,len(data)):
        if user[1] == data[i]['a']:
            count = count+1
            deliver.append(data[i])

    f = open('messages.txt', 'w')
    for i in range(0,len(data)):
        if user[1] != data[i]['a']:
            f.write(data[i]['a'])
            f.write(':')
            f.write(data[i]['b'])
            f.write(':')
            f.write(data[i]['c'])
            f.write('\n')
    f.close()

    if count == 0:
        message = "\n>> Welcome back "+user[1]+", you have no new messages.\n"
    else:
        message = "\n>> Welcome "+user[1]+", you have "+str(count)+" messages waiting :\n"
        message += str(getMess(deliver))
    return message

# function that allows the user to log off using the address that the user is on to 
# trace them. 
def logOut(command,address):
	for i in range(0,len(SESSION_ID)):
		if address[1] == SESSION_ID[i]['b']:
			name = SESSION_ID[i]['a']
			ONLINE.remove(name)
			del SESSION_ID[i]
			message = "\n>> Session closed.\n"
		else:
			message = "\n>> You have to be logged in to log out!\n"

	return message

# function to send messages to other users
def sendMess(command,address):
    data = command
    message = ''
    mess2 = (" ").join(data[2:])

    for i in range(0,len(SESSION_ID)):
        if address[1] == SESSION_ID[i]['b']:
            name = SESSION_ID[i]['a']

            f = open('messages.txt', 'a')
            f.write(data[1])
            f.write(':')
            f.write(name)
            f.write(':')
            f.write(mess2)
            f.write('\n')
            f.close()

            if name in ONLINE:
                message = ''
            else:
                message = "\n>> "+data[1]+" is offline, message will be saved for future delivery."

        else:
            message = "\n>> Message not sent, you may not be signed in.\n"
    
    return message

# function to format the messages retrieved
def getMess(messages):
    data = messages
    message = ''

    for i in range(0,len(data)):
        message += ">>     "+str(data[i]['b'])+" : "+str(data[i]['c'])+"\n"
    return message

# function to check for new messages, to be called by the server every time a
# command is entered by the client... it is not working correctly.
def iMess(address):
	user = address

	for i in range(0,len(SESSION_ID)):
		if user[1] == SESSION_ID[i]['b']:
			name = SESSION_ID[i]['a']

	user = command
	data = []
	count = 0
	f = open('messages.txt', 'r')
	mLines = f.readlines()

	for line in mLines:
		line = line.strip()
		tmp = line.split(':')
		uMess = {'a':tmp[0], 'b':tmp[1], 'c':tmp[2]}
		data.append(uMess)
	f.close()

	deliver = []

	for i in range(0,len(data)):
		if user[1] == data[i]['a']:
			count = count+1
			deliver.append(data[i])

	f = open('messages.txt', 'w')
	for i in range(0,len(data)):
		if user[1] != data[i]['a']:
			f.write(data[i]['a'])
			f.write(':')
			f.write(data[i]['b'])
			f.write(':')
			f.write(data[i]['c'])
			f.write('\n')
			f.close()

	if count == 0:
		message = ""
	else:
		message = str(getMess(deliver))
	return message

# function to tell the user who is online
def whoIsOn():
	uol = set()
	nol = set()

	for i in range(0,len(USERS)):
		for j in range(0,len(ONLINE)):
			if ONLINE[j] in USERS:
				uol.add(ONLINE[j])

	for i in range(0,len(USERS)):
		if USERS[i] not in ONLINE:
			nol.add(USERS[i])

	message = "\n>> Users "+str(uol)+" are online\n>> Users "+str(nol)+" are NOT online"
	
	return message

# function to display the accepted commands for the user
def help():
    message = "\n>> The following commands are supported:\n>>    logIn <username>\n>>    whoIsOn\n>>    send <username> <message>\n>>    logOut <username> <session ID>\n>>    help\n>> Remember commands are case sensitive\n"
    return message



