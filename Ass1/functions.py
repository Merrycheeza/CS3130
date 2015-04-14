#!/usr/bin/env python3
###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 1      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################



# print off of the main menu which allows users
# to select an option
def menu():
    print('--')
    print('Employee FMS\n')
    print('Select one of the following:\n')
    print('  1) Add a new employee')
    print('  2) Search for an employee')
    print('  3) Remove an employee from FMS')
    print('  4) Display entire employee FMS')
    print('  5) Quit\n')

def menu2():
    print('Select one of the following:\n')
    print('  1) Add a new employee')
    print('  2) Search for an employee')
    print('  3) Remove an employee from FMS')
    print('  4) Display entire employee FMS')
    print('  5) Quit\n')

# function to open the database and turn it into
# a useable format for the rest of the functions
def readDB():
    data = []
    f = open('database.txt','r')
    dbLines = f.readlines()
    for line in dbLines:
        line = line.strip()
        tmp = line.split(':')
        record = {'a':tmp[0] , 'b':tmp[1], 'c':tmp[2], 'd':tmp[3]}
        data.append(record)
    f.close()
    return data

# function to add a line to the database text file
def addEmp():
    data = readDB()

    userID = True

    print("\n--Add an Employee--\n")
    while(userID):
        print("Please enter a new, 4 digit, user ID number: ", end = '')
        uid = input()

        if uid.isdigit():

            if len(uid) == 4:

                if checkEmp(uid) == 2:
                    print("I'm sorry that number is already in use.")
                    print("Please try again.")

                else:
                    print("Enter employee first name: ", end = '')
                    fname = input()
                    if fname.isalpha():
                        userID = False
                        myloop = True
                    
                    while(myloop):
                        print("Enter employee last name: ", end = '')
                        lname = input()
                        if lname.isalpha():
                           myloop = False
                           myloop2 = True

                    while(myloop2):
                        print("Enter employee department: ", end = '')
                        dept = input()
                        if dept.isalpha():
                            newUser = [uid,":",fname,":",lname,":",dept]
                            database = open("database.txt","a")
                            database.writelines(newUser)
                            database.write("\n")
                            database.close()
                            print('\nAddition Successful\n')
                            myloop2 = False

                            print("Would you like to add another? (y/n) ", end='')
                            loop = input()
                            if loop in ['y','Y','n','N']:
                                if loop in ['y', 'Y']:
                                    addEmp()
                                else:
                                    continue
                            else:
                                print("Error: returning to main menu\n")

            else:
                print("Please enter a 4 digit number.")
        else:
            print("You did not enter a number")
    print('')
    menu2()   
    return

# function to check if a user ID is already in use
def checkEmp(uid):
    data = readDB()
    value = 1

    for i in range(0,len(data)):
        if uid == data[i]['a']:
            value = 2
    return value


# function to display the details of an employee based
# on the ID the user inputs
def searchEmp():
    data = readDB()

    print("\n--Employee Search--\n")
    print("Please enter the user ID number: ", end ='')
    emp = input()

    for i in range(0,len(data)):
        a = data[i]['a']
        b = data[i]['b']
        c = data[i]['c']
        d = data[i]['d']


        if emp == a:
            print("Employee ID# : ", a)
            print("First name   : ", b)
            print("Last Name    : ", c)
            print("Department   : ", d)
            print('')
            break
            
        if i == (len(data)-1):
            print("I'm sorry, that employee number does not seem to be in use.\n")

    print("Would you like to try again? (y/n) ", end='')
    loop = input()
    if loop in ['y','Y','n','N']:
        if loop in ['y', 'Y']:
            searchEmp()
    else:
        print("Error: returning to main menu\n")
    
    print('')
    menu2()

    return

# function to remove an employee from the database
# FIRED!!
def remEmp():
    data = readDB()

    userID = True

    print("\n--Remove an Employee--\n")

    while(userID):
        print("Please enter the 4 digit user ID number: ", end='')
        emp = input()

        if emp.isdigit():

            if len(emp) != 4:
                print("Sorry, invalid number.")

            elif checkEmp(emp) != 2:
                print("Sorry, that is not a valid employee number.")
                print("Would you like to try again? (y/n) ", end = '')
                loop = input()
                if loop in ['y','Y','n','N']:
                    if loop in ['y', 'Y']:
                        remEmp()
                    else:
                        userID = False
                        print("Returning to the main menu")
                        break

            else:
                for i in range(0,len(data)):
                    if emp == data[i]['a']:                    
                        del data[i]
 
                f = open('database.txt', 'w')
                for i in range(0,len(data)):
                    f.write(data[i]['a'])
                    f.write(':')
                    f.write(data[i]['b'])
                    f.write(':')
                    f.write(data[i]['c'])
                    f.write(':')
                    f.write(data[i]['d'])
                    f.write('\n')
                f.close()

                print("Removal Successful\n")
                print("Would you like to remove another? (y/n) ", end = '')
                loop = input()
                if loop in ['y','Y','n','N']:
                    if loop in ['y', 'Y']:
                        remEmp()
                    else:
                        userID = False
                        continue

        else:
            print("That user ID does not seem to be valid.")

    print('')
    menu2()
    return

# funtion to display the entire employee database
def dispDB():
    data = readDB()
    print('\n--Current Employees--\n')
    print("|   ID   | First Name |  Last Name  |  Department |")
    print("---------------------------------------------------")
    for i in range(0,len(data)):
        a = data[i]['a']
        b = data[i]['b']
        c = data[i]['c']
        d = data[i]['d']
        print("| {0:^6s} | {1:^10s} | {2:^11s} | {3:^11s} |".format(a,b,c,d))
    print('')
    return

