###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Final Project      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################

For this final project, I chose to create a choose your own adventure story. The story itself is static and the players can move through it by making choices on each page.

At any time during their progression, the players have the option to display a help menu or quit. Each page has two choices that the player can decide between, so the client and server functions remain static throughout the whole program as well, but they seem to be more dynamic because the choices change for the player.

This file includes 2 databases:
	1) users {username, password, current location}
	2) Story {page number, paragraph, choice page 1, choice page 2}
	
2 Textfiles:
  1) Title page
  2) Help
  
2 Function files:
  1) main.py
  2) functions.py

To begin the program open a server window and type: python3 main.py server
In a windows cmd window type: main.py server
Then open a client window and type: python3 main.py client
In a Windows cmd window type: main.py client

Enjoy!!!

Things that are not quite working right/Unexpected problems:
1) There were a few pages still under construction at the submission of this project but there are enough finished to show how the program works.
2) The create account function sort of relies on the user's maturity in not creating account all willy nilly whenever s/he pleases in the game.
	- A possible fix for this is to make sure that the user is only logged in as guest when creating a new account.
	- Fixed this.. you now have to be logged in as guest to make an account

On the bright side... the story is a bit funny.
