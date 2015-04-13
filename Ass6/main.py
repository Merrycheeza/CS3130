###################################
#				  #
# Class: 	CS3130		  #
# Assignment: 	Assignment 6      #
# Author:	Samara Drewe	  #
# 		4921860		  #
#				  #
###################################

#!/usr/bin/env python3.4

import functions

# Main program to run all the functions and print menu
def main():

    running = True
    functions.menu()
    
    while(running):
        print('>>> ', end = '')
        select = input()

        if select == '1':
            functions.giSPTsx()
        
        elif select == '2':
            functions.giSP500()

        elif select == '3':
            functions.giDow()

        elif select == '4':
            functions.giNasdaq()

        elif select == '5':
            functions.giDollar()

        elif select == '6':
            functions.giGold()

        elif select == '7':
            functions.giCrude()

        elif select == '8':
            running = False

        else:
            print('Please choose a number between 1-8')

    print('--')
        
main()
