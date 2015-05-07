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
# this portion of the program handles the client as well as the server

import random, socket, sys, argparse, functions

end = '.' #the server uses this to see if the information is complete
host = ('127.0.0.1') #hard coded the host and port because windows is hard
port = 2015

# this function is the TCP server
# it handles all the requests from the client    
def server(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)

    print('Server is listening at ', sock.getsockname())    
    while True:
        print('Waiting for a connection')
        sc, sockname = sock.accept()
        print('Connection accepted from, ', sockname)
        message = functions.recvall(sc)
        print('\nMessage: ', repr(message))

        # +100 series protocols for adding an employee to the database
        # +110 is a success
        # -101 is a failure
        if '+100' in message:
            reply = functions.serverAddEmp(message)
            if reply == 1:
                sc.sendall(b'-101: This user ID already exists please try again.')
            else:
                sc.sendall(b'+100: Employee added successfully.')

        # +200 series protocols for searching the database
        # +220 is a success
        # -202 is a failure
        elif '+200' in message:
            reply = functions.serverSearchEmp(message)
            sc.sendall(reply)      
     
        # +300 series protocols for removing an employee from the database
        # +330 is a success
        # -303 is a failure
        elif '+300' in message:
            reply = functions.serverRemoveEmp(message)
            sc.sendall(reply)
                
        # +400 series protocols for removing an employee from the database
        # +440 is a success
        # -404 is a failure     
        elif '+400' in message:
            reply = functions.serverDisplayEmp()
            if reply == None:
                sc.sendall(b'-404: Database not found')
            else:
                sc.sendall(reply.encode('ascii'))
   
        # +500 series protocol for quitting
        # There is only success!!
        elif '+500' in message:
            sc.sendall(b'Server is closing.')
            sc.close()
            print('Socket is now closed.')
            exit(0)

        sc.close()
        print('Socket is now closed.')

# this function is the TCP client
# it allows the user to make requests from the server
# and interact with the database
def client(port):
    functions.mainMenu()
  
    while True:
        functions.menu()
        print("Option? ", end = '')
        choice = input()
        print("--\n")
        
        if int(choice) == 1:
            functions.addEmp()
        elif int(choice) == 2:
            functions.searchEmp()
        elif int(choice) == 3:
            functions.removeEmp()
        elif int(choice) == 4:
            functions.displayEmp()
        elif int(choice) == 5:
            functions.quit()
        else:
            print('Your choice is not valid.')
            

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=2015,
    help='TCP port (default 2015)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
