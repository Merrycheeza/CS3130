###################################
# #
# Class: CS3130 #
# Assignment: Lab Assignment 2 #
# Author: Samara Drewe #
# 4921860 #
# #
###################################
#!/usr/bin/env python3
import sys, re
running = True
# prints the menu
print("--")
print("Phone Number ")
print(" ")
while(running):
# asks for the number
print("Enter phone number: ", end = "")
phone = input()
# checks to see if it's a blank line
if(phone == ""):
running = False
break
else:
#takes out the parenthesis and spaces
phone1 = re.sub('[\s+\(\)]', '', phone)
# checks the length, if it is lesser or greater than 10 digits, it's not a phone number
if len(phone1) == 10:
# checks length again after taking out everything that isn't a number
if(len(re.sub('[^0-9]',"", phone1)) == 10):
print("Number is " + "(" + phone1[0:3] + ")" + " " + phone1[3:6] + " " + phone1[6:])
# if it is not 10 digits, there were characters that were not numbers in the phone number
else:
print("Characters other than digits, hypens, space and parantheses detected")
# length not 10 digits, not a phone number
else:
print("Sorry phone number needs exactly 10 digits")
print("--")
