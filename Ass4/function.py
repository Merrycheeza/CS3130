#!/usr/bin/env python3
###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 4      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################
#
# this portion of the program contains the functions
# called by both the client and the server

import random, socket, sys, argparse

end = '.'
host = ('127.0.0.1')
port = 2015

def mainMenu():
    print("\n--\n")
    print("Employee FMS\n")

def menu():
    print("Select one of the following:\n")
    print("1) Add a new employee")
    print("2) Search for an employee")
    print("3) Remove an employee from FMS")
    print("4) Display entire employee FMS")
    print("5) Quit\n")

# function for handling communication
# between the client and server
def recvall(sock):
    message = ''
    while end not in message:
        data = sock.recv(4096)
        data = data.decode('ascii')
        message += data
    
    return message

# function to open the database and turn it into
# a dictionary for the rest of the functions       
def readDB():
    data = {}
    f = open('database.txt','r')
    for line in f:
        line = line.strip()
        ID, rest = line.split(':',1)
        data[ID] = rest.split(":",2)
    f.close()
    return data

# function to check if a user ID is
# currently in use
def checkEmp(uid):
    data = readDB()
    value = 1

    for i in range(0,len(data)):
        if uid == data[i]['a']:
            value = 2
    return value

# function to add an employee to the database
# this is protocol +100 on the client side
# it checks to make sure the data is valid
# before passing it onto the server
# it also offers to add another
def addEmp():
    print("\n--Add an Employee--\n")
    loop1 = True

    while(loop1):
        print("Enter a 4 digit user ID number: ", end = '')
        uid = input()

        if uid.isdigit():

            if len(uid) == 4:
                uid += ':'
                loop1 = False
                loop2 = True

                while(loop2):
                    print("Enter employee first name: ", end = '')
                    fname = input()
                    if fname.isalpha():
                        fname += ':'
                        loop2 = False
                        loop3 = True
                    
                    while(loop3):
                        print("Enter employee last name: ", end = '')
                        lname = input()
                        if lname.isalpha():
                            lname += ':'
                            loop3 = False
                            loop4 = True

                    while(loop4):
                        print("Enter employee department: ", end = '')
                        dept = input()
                        if dept.isalpha():
                            loop4 = False
                            dept += end
                            print('\n')
               
            else:
                print("That is not a 4 digit number.")
        else:
            print("You did not enter a number")

    employee = uid + fname + lname + dept

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    send = '+100:' + employee
    message = send.encode('ascii')
    sock.sendall(message)
    reply = recvall(sock)
    reply = reply.replace('.','')
    sock.close()

    print(str(reply))

    print("\nWould you like to add another? (y/n) ", end = '')
    choice = False
    while choice == False:
        answer = input()
        print('\n')
        if answer in['y','n','Y','N']:
            choice = True
        else:
            print("Invalid input.") 
            choice = False                   
                   
    if answer in ['y','Y']:
        addEmp()


# function to add an employee to the database
# this is protocol +100 on the server side
# it checks the database to see if the user ID
# is already in use and then appends the database
def serverAddEmp(message):
    
    print(message)
    protocol, uid, fname, lname, dept = message.split(':')
    
    data = readDB()
    user = []
    
    if uid in data:
        reply = 1
              
    else:
        dept = dept.replace('.','')
        user = [uid,":",fname,":",lname,":",dept]
        database = open("database.txt","a")
        database.writelines(user)
        database.write("\n")
        database.close()
        reply = 0

    return reply

# function to search for an employee ID on the database
# this is protocol +200 on the client side
# and offers to allow another search
def searchEmp():
    print("\n--Employee Search--\n")
    print("Please enter an Employee ID: ", end = '')
    uid = str(input())
    uid = uid + end
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    send = '+200:' + uid
    message = send.encode('ascii')
    sock.sendall(message)
    reply = recvall(sock)
    reply = reply.replace('.','')
    sock.close()
    print(str(reply))
    
    print('\nWould you like to find another employee? (y/n) ', end = '')
    choice = False
    while choice == False:
        answer = input()
          
        if answer in['y','n','Y','N']:
            choice = True
        else:
            print("Invalid input.") 
            choice = False
             
    if answer in ['y','Y']:
        searchEmp()

# function to search for an employee ID on the database
# this is protocol +200 on the server side
# it checks the database to see if the
# employee ID provided is in there
# -202 for invalid ID
# +220 for a match
def serverSearchEmp(message):
    print(message)
    data = readDB()
    user = []

    protocol, uid = message.split(':')
    uid = uid.replace('.','')
    if uid in data.keys():
        reply = "\n+220:\nEmployee ID# : " + uid
        reply += "\nFirst name   : " + data[uid][0]
        reply += "\nLast name    : "+data[uid][1]
        reply += "\nDepartment   : " + data[uid][2]
        reply += end

    else:
        reply = "\n-202: Not a valid employee ID."

    reply = reply.encode('ascii')   
    return reply

# function to remove an employee from the database
# this is protocol +300 on the client side
# it simply takes the input and passes it to the
# server for validation and then offers to check another
def removeEmp():
    print("\n--Remove an Employee--\n")
    print("Please enter the 4 digit user ID number: ", end='')
    uid = str(input())
    uid += end

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    send = '+300:' + uid
    message = send.encode('ascii')
    sock.sendall(message)
    reply = recvall(sock)
    reply = reply.replace('.','')
    print(str(reply))
    sock.close()

    print("Would you like to remove another? (y/n) ", end = '')
    loop = input()
    if loop in ['y','Y','n','N']:
        if loop in ['y', 'Y']:
            removeEmp()

# function to remove an employee from the database
# this is protocol +300 on the server side
# it takes the message from the client and
# removes a match from the database
# -303 if there is no match
def serverRemoveEmp(message):
    print(message)
    data = readDB()
    user = []

    protocol, uid = message.split(':')
    uid = uid.replace('.','')
    if not uid in data.keys():
        reply = b'-303: Employee ID not found.'
    else:
        reply = b'+330: You have successfully removed the employee.'
        del data[uid]
        f = open("database.txt","w+")
        for i,j in data.items():
            f.write(i + ':' + ':'.join(j) + '\n')
        f.close()
    return reply

#display all user from the databases protocol +400    
def displayEmp():
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    send = '+400:' + end 
    message = send.encode('ascii')
    sock.sendall(message)
    reply = recvall(sock)
    reply = reply.replace('.','')
    print (str(reply))
    sock.close()

# function to display the database
# this is protocol +400 on the server side
def serverDisplayEmp():

    data = readDB()
    user = []

    reply = "+440:\n"
    reply += "|   ID   | First Name |  Last Name  |  Department |\n"
    reply += "---------------------------------------------------\n"
    for i in data.keys():
        a = i
        b = data[i][0]
        c = data[i][1]
        d = data[i][2]
        reply += "| {0:^6s} | {1:^10s} | {2:^11s} | {3:^11s} |\n".format(a,b,c,d)
    reply += "\n"
    reply += end
    return reply

# function to quit
# this is protocol +500
def quit():
    print('Thank you for using Employee FMS')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    send = '+500' + end
    message = send.encode('ascii')
    sock.sendall(message)
    reply = recvall(sock)
    reply = reply.replace('.','')
    sock.close()
    print(str(reply))
    exit(0)

