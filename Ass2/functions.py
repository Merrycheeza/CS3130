#!/usr/bin/env python3
###################################
#				  
# Class: 	CS3130		  
# Assignment: 	Assignment 1      
# Author:	Samara Drewe	  
# 		4921860		  
#				  
###################################

import sys

# function to print out the main title of the program
def title():
    print('--')
    print('Word Frequency Table Generator\n')
    print('Enter name of file to process : ', end='')

# function to get the data from the outside source, returns the text
def getFile():
    filename = input()
    print('--')

    value = True

    while(value):
        try:
            data = open(filename,"r")
            text = data.read()
            data.close()
            value = False
            
        except FileNotFoundError:
            print('Error: File not found')
            value = False
    return text

# function to take the text and process it, removing punctuation and turning it
# into a list. At the same time it counts the frequency of the words in the list
# then it calls two additional functions to print out the results and passes
# the parameters to each of them
def process(f):
    data = []
    count = []
    text = f

    text = text.replace("."," ")
    text = text.replace(","," ")
    text = text.replace(";"," ")
    text = text.replace("?"," ")
    text = text.replace("!"," ")
    text = text.replace('"'," ")
    text = text.replace("-"," ")

    text = text.strip().split()

    for i in range(0,len(text)):
        text[i] = text[i].lower()
        new = True

        for j in range(0,len(data)):
            if data[j] == text[i]:
                count[j] = count[j]+1
                new = False
        if new:
            data.append(text[i])
            count.append(1)

    print('file processing complete.\n')
    wordFreq(data, count)
    wordHist(text, data, count)

# function to print out the word frequency chart
def wordFreq(data, count):
    print('Word Frequency Table')
    print('-----------------------------------')
    for i in range(0,len(data)):
        print("%-25.25s %-5i" % (data[i],count[i]))
    print('')
    return

# function to print out the histogram
def wordHist(text, data, count):
    print('HISTOGRAM\n')
    for i in range(0,len(data)):
        if (count[i] > 10):
            print("{0:<15s}".format(data[i])+"|"+"X"*10+"({0})".format(count[i]))
        else:
            print("{0:<15s}".format(data[i])+"|"+"X"*count[i])
    print('')

    return
