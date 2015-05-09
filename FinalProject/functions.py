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
# this portion of the program handles the functions used by client and server

import random, socket, sys, argparse, re

host = ('127.0.0.1')
port = 2015

ONLINE = []
SESSION_ID = []
USERS = ['guest','Samara', 'Franco', 'Coca', 'Tulip']

# function to read the story database
def readDB():
    data = []
    f = open('story.txt','r')
    dbLines = f.readlines()
    for line in dbLines:
        line = line.strip()
        tmp = line.split(':')
        record = {'a':tmp[0] , 'b':tmp[1], 'c':tmp[2], 'd':tmp[3]}
        data.append(record)
    f.close()
    return data

# function to read the user database
def userDB():
    data = []
    f = open('user.txt','r')
    dbLines = f.readlines()
    for line in dbLines:
        line = line.strip()
        tmp = line.split(':')
        record = {'a':tmp[0] , 'b':tmp[1], 'c':tmp[2]}
        data.append(record)
    f.close()
    return data

# function to print the title screen for the client    
def titleScreen():
    data = []
    f = open('title.txt', 'r')
    tLines = f.readlines()
    for line in tLines:
        line = line.strip()
        data.append(line)
    f.close()
    print('\n')
    for i in range(0,22):
        print(data[i])   

# function to log in an account holder or guest
def login(command,address):
    user = command[1]

    if user not in USERS:
        message = ">> User "+user+" is not a valid account."

    elif user in ONLINE:
        message = ">> Sorry, that user is already logged in."

    else:
        if user == 'guest':
            message = ">> Welcome "+user+" please remember that all commands are case sensitive."
            message+= "\n>> You may use help, save, and quit at any time."
            message+= "\n>> To create a new account, please type: create <username> <password>"
            record = {'a':user,'b':address[1]}
            ONLINE.append(user)
            SESSION_ID.append(record)
        else:
            cuser = checkPass(command)
            if cuser['a'] == 'invalid':
                message = 'Sorry your password is invalid'
            else:
                place = cuser['c']
                message = 'Last time on "Peanut Butter Jelly Time"...\n'
                message += '\n'
                message += placeHolder(place)
                record = {'a':user,'b':address[1]}
                ONLINE.append(user)
                SESSION_ID.append(record)
    return message

# function to check the password of an account
def checkPass(command):
    user = command
    data = userDB()
    cuser = []
    
    for i in range(0,len(data)):
        if user[2] == data[i]['b']:
            cuser = data[i]
            break
        else:
            cuser = data[0]
       
    return cuser

# function to get the user details to pass on to other functions
def getUser(address):
    data = userDB()
    cuser = []
    for i in range(0,len(SESSION_ID)):
        if address[1] == SESSION_ID[i]['b']:
            name = SESSION_ID[i]['a']

    for i in range(0,len(data)):
        if name == data[i]['a']:
            cuser = data[i]

    return cuser

# function to advance in the story
# this function calls readDB, getUser,
# placeHolder, and updateUser
def chooseNext(command, address):
    data = readDB()
    param = int(command[0])
    addy = address[1]

    if addy in SESSION_ID:
        user = getUser(address)
        for i in range(0,len(data)):
            if user['c'] == data[i]['a']:
                if param == 1:
                    page = data[i]['c']
                else:
                    page = data[i]['d']

        message = placeHolder(page)
        updateUser(user, page)

    else:
        message = "Sorry, you are not logged in."

    return message

# function to update the user as s/he advances in the story
def updateUser(user, page):
    data = userDB()
    user['c'] = page

    for i in range(0,len(data)):
        if user['a'] == data[i]['a']:
            del data[i]
            data.append(user)

    f = open('user.txt', 'w')
    for i in range(0,len(data)):
        f.write(data[i]['a'])
        f.write(':')
        f.write(data[i]['b'])
        f.write(':')
        f.write(str(data[i]['c']))
        f.write('\n')
    f.close()

# function to print out the page the user is currently at    
def placeHolder(place):
    data = readDB()

    for i in range(0,len(data)):
        if place == data[i]['a']:
            message = data[i]['b']
            message = re.sub(';','\n',message)
            break
        else:
            message = "Page not found."

    return message

# function to quit
def logout(command,address):
    message = ''
    for i in range(0,len(SESSION_ID)):
        if address[1] == SESSION_ID[i]['b']:
            name = SESSION_ID[i]['a']
            ONLINE.remove(name)
            del SESSION_ID[i]
            message = ">> Session closed."
        else:
            message = ">> You have to be logged in to log out!"

    return message

# function to force quit a user if they disconnected
# not finished
def fquit(command):
    return

# function to print out the help menu
def help():
    data = []
    message = ''
    f = open('help.txt', 'r')
    tLines = f.readlines()
    for line in tLines:
        line = line.strip()
        message += line
        message += '\n'
    f.close()
    return message
       
def createAccount(command):
    data = userDB()
    user = command

    for i in range(0,len(data)):
        if user[1] == data[i]['a']:
            message = "Sorry that username is already taken."
        else:
            newUser = [user[1],":",str(user[2]),":",str(0)]
            users = open("user.txt","a")
            users.writelines(newUser)
            users.write("\n")
            users.close()
            USERS.append(user[1])
            message = "\nAddition Successful. Please type quit and log in using your new account.\n"
            
    return message
