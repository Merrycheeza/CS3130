###################################
#				  #
# Class: 	CS3130		  #
# Assignment: 	Assignment 6      #
# Author:	Samara Drewe	  #
# 		4921860		  #
#				  #
###################################

#!/usr/bin/env python3.4

import requests, re, sys
from bs4 import BeautifulSoup 

# prints the menu
def menu():
    print('--')
    print('Market Information')
    print('')
    print('Select one of the following :')
    print('')
    print('  1) S&P TSX')
    print('  2) S&P 500')
    print('  3) Dow Jones')
    print('  4) Nasdaq')
    print('  5) CAD/USD')
    print('  6) Gold')
    print('  7) WTI Crude')
    print('  8) Quit')
    print('')

# grabs the data from the website and compiles it into useable information
def getRequest():
    r = requests.get('http://www.theglobeandmail.com/globe-investor/')
    data = r.content

    soup = BeautifulSoup(data)

    return soup

# function that extracts the required information for option 1
# using BeautifulSoup's find function I was able to grab the 
# individual values to print out in each of my options
def giSPTsx():
    print('S&P TSX -- ', end = '')
    s = getRequest()
    currVal = s.find('div',{'data-id':'593253'}).find('div',{'class':'prominent less-prominent last-value chars9'}).text
    change = s.find('div',{'data-id':'593253'}).find('div',{'class':'change'}).text
    time = s.find('div',{'data-id':'593253'}).find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 2
def giSP500():
    print('S&P 500 -- ', end = '')
    s = getRequest()
    currVal = s.find('div',{'data-id':'575769'}).find('div',{'class':'prominent less-prominent last-value chars8'}).text
    change = s.find('div',{'data-id':'575769'}).find('div',{'class':'change'}).text
    time = s.find('div',{'data-id':'575769'}).find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 3
def giDow():
    print('Dow Jones -- ', end = '')
    s = getRequest()
    currVal = s.find('div',{'data-id':'599362'}).find('div',{'class':'prominent less-prominent last-value chars9'}).text
    change = s.find('div',{'data-id':'599362'}).find('div',{'class':'change'}).text
    time = s.find('div',{'data-id':'599362'}).find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 4
def giNasdaq():
    print('Nasdaq -- ', end = '')
    s = getRequest()
    currVal = s.find('div',{'data-id':'579435'}).find('div',{'class':'prominent less-prominent last-value chars8'}).text
    change = s.find('div',{'data-id':'579435'}).find('div',{'class':'change'}).text
    time = s.find('div',{'data-id':'579435'}).find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 5
def giDollar():
    print('CAD/USD -- ', end = '')
    s = getRequest()
    currVal = s.find('div',{'class':'currency'}).find('span', 'prominent less-prominent').text
    change = s.find('div',{'data-id':'Currencies'}).find('div',{'class':'change'}).text
    time = s.find('div',{'data-id':'Currencies'}).find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 6
def giGold():
    print('Gold -- ', end = '')
    s = getRequest()
    currVal = s.find_all('div',{'data-id':'Commodities'})[0].find('div',{'class':'value prominent less-prominent'}).text
    change = s.find_all('div',{'data-id':'Commodities'})[0].find('div',{'class':'change'}).text
    time = s.find_all('div',{'data-id':'Commodities'})[0].find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)

# function that extracts the required information for option 7
def giCrude():
    print('WTI Crude -- ', end = '')
    s = getRequest()
    currVal = s.find_all('div',{'data-id':'Commodities'})[1].find('div',{'class':'value prominent less-prominent'}).text
    change = s.find_all('div',{'data-id':'Commodities'})[1].find('div',{'class':'change'}).text
    time = s.find_all('div',{'data-id':'Commodities'})[1].find('span', 'timing update-info').text
    print(currVal, "--", change, "--", time)
