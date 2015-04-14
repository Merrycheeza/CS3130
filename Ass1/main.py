#!/usr/bin/env python3
###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 1      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################

import functions

def main():
    functions.menu()
    running = True

    while(running):
        print('Option? ', end = '')
        option = input()

        if option == '1':
            functions.addEmp()

        elif option == '2':
            functions.searchEmp()

        elif option == '3':
            functions.remEmp()

        elif option == '4':
            functions.dispDB()

        elif option == '5':
            print('Thank you for using Employee FMS')
            running = False

        else:
            print("I'm sorry, I do not recognize that number\n")

    print('--')

    
main()
