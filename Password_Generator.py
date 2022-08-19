#!/usr/bin/python

import random

#Create a password generator


#Create dictionary of possible characters
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e',f'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e',f'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols =['!','@','#','$','%','^','&','*']
#Ask for length of password
len_pass = int(input("How long do you want your password to be? "))
#ask if password should include symbols
pass_sym = input("Would you like to include symbols in your password? [y/n] ")
#ask if password should include numbers
pass_num = input("Would you like to include numbers in your password? [y/n] ")

def which_pass():
	if pass_sym.upper() == 'Y':
		if pass_num.upper() == 'Y':
			print("all")
			all_pass()
		else:
			letters_sym_pass()
	elif pass_num.upper() == 'Y':
		letters_num_pass()
	else:
		letters_only()
		
#create a variable that is an empty string that we'll use to create the password
#create a for loop that will iterate the amount of characters that the user would like for their password
#add a random character from our character dictionary to our password string every time it iterates through the for loop
#print the password

#if user wants letters, symbols and numbers, call this function
def all_pass():
	password = ''
	for n in range(0, int(len_pass)):
		password += random.choice(characters)
	print(password)

#if user wants letters and numbers, call this function
def letters_num_pass():
	password = ''
	for n in range(0, int(len_pass)):
		password += random.choice(letters + numbers)
	print(password)
	
#if user wants letters and symbols, call this function
def letters_sym_pass():
	password = ''
	for n in range(0, int(len_pass)):
		password += random.choice(letters + symbols)
	print(password)

#if user wants letters only, call this function
def letters_only():
	password = ''
	for n in range(0, int(len_pass)):
		password += random.choice(letters)
	print(password)

#call this function to begin the process	
which_pass()
