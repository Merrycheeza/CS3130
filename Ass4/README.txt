###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 4      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################

This program is a continuation of the employee database from assignment 1. 
This time it makes use of a TCP server and client. The user picks the function he or she wishes to manipulate the database with.
As in assignment 1, the commands include:
1) Add
2) Search
3) Remove
4) Display

Included are 4 files:
- database.txt
    - This file contains all of the employees and their details
- functions.py
    - This file contains all of the functions written for both the client and server in the program
- main.py
    - This file handles the server and client respectively
- protocols.txt
    - This file contains the protocol numbers used in the program

I used Windows to make this and the start up commands are different than in linux.

To start in Windows type:
main.py server (for the server)

and

main.py client (for the client)

To start in Linux (I hope) type:

python3 main.py server

and

python3 main.py client

The program automatically assigns the host 127.0.0.1 and port 2015
