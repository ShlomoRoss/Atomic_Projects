#!/usr/bin/python

import sys
import time
import random
from colorama import Fore, Back, Style


#some cool ascii art as variables to go along with the game. These variables will be printed and shown throughout the game 
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  


#How to print characters one by one on a single line
def char_print(text):
	for c in text:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
		
#Run this function to ask player which option they would like to choose
def choose():
	print(Fore.YELLOW + Style.BRIGHT)
	char_print("Choose Rock, Paper or Scissors: ")
	choice = input()
	if choice.upper() == "ROCK":
		chose_rock()
	elif choice.upper() == "PAPER":
		chose_paper()
	else:
		chose_scissors()
		
#If the player chse rock, use this funtion to run the logic required to play
def chose_rock():
	print(Fore.MAGENTA + rock)
	time.sleep(1)
	result = random.choice(["rock", "paper", "scissors"])
	if result == "rock":
		print(Fore.MAGENTA + rock)
		print(Fore.YELLOW + Style.NORMAL + "It's a tie! Choose again")
		choose()
	elif result == "paper":
		print(Fore.BLUE + paper)
		print(Fore.RED + "Paper beats rock, you lose!")
		yes_no()
	else:
		print(Fore.CYAN + scissors)
		print(Fore.GREEN + "Rock beats scissors, you win!")
		yes_no()
		
#If the player chose paper, use this funtion to run the logic required to play
def chose_paper():
	print(Fore.BLUE + paper)
	time.sleep(1)
	result = random.choice(["rock", "paper", "scissors"])
	if result == "rock":
		print(Fore.MAGENTA + rock)
		print(Fore.GREEN + "Paper beats rock, you win!")
		yes_no()
	elif result == "paper":
		print(Fore.BLUE + paper)
		print(Fore.YELLOW + Style.NORMAL + "It's a tie! Choose again")
		choose()
	else:
		print(Fore.CYAN + scissors)
		print(Fore.RED + "Scissors beats paper, you lose!")
		yes_no()
		
#If the player chose scissors, use this funtion to run the logic required to play
def chose_scissors():
	print(Fore.CYAN + scissors)
	time.sleep(1)
	result = random.choice(["rock", "paper", "scissors"])
	if result == "rock":
		print(Fore.MAGENTA + rock)
		print(Fore.RED + "Rock beats scissors, you lose!")
		yes_no()
	elif result == "paper":
		print(Fore.BLUE + paper)
		print(Fore.GREEN + "Scissors beats paper, you win!")
		yes_no()
	else:
		print(scissors)
		print(Fore.YELLOW + Style.NORMAL + "It's a tie! Choose again")
		choose()
		
#After the game is complete, ask the player if they want to play again
def yes_no():
    response = input("Do you want to play again? ")
    if response.upper() == "YES":
        choose()
    else:
        char_print("Have a great day! Come back soon!")
        
print(Fore.YELLOW + Style.BRIGHT)       
print("Welcome to Rock, Paper, Scissors")
print(rock)
time.sleep(0.5)
print(paper)
time.sleep(0.5)
print(scissors)
choose()


