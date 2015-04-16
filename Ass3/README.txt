###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 3      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################

This is a messenging program that interacts between server and client. 
1) Add
2) Search
3) Remove
4) Display

Included are 4 files:
- messages.txt
    - This file contains all of the messages that are sent between clients.
- functions.py
    - This file contains all of the functions written for the program.
- server.py
    - This file handles the client and server and their communication.
- protocol.txt
    - This file is a detailed explaination of the program and the expectations of what it should do.
    
Unexpected problems (can we call these features?):
- If two people are logged in and trying to message each other, it will tell the one that logged in last that they are not online. It will still send the message but the return message is wrong and I couldn't figure out why.
- The instant messenger isn't exactly instant. The client has to log in and out because I couldn't get the iMess() function to work properly.

To start type:

python3.4 server.py
