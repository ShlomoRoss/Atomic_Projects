#!/usr/bin/python
import time

#The purpose of this program is to help someone choose their new favorite baseball team
#We will help them choose their team by asking them some questions abot their preferences
#Once all of their answers are recorded, we will use conditional statements to select a team

print('''
@@@@@@@@@@@@@@@O°.°°.O@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@o.°°.°O@@@@@@@@@@@@@@@
@@@@@@@@@@@###°.o###O.°#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@#@@#°.O###o.°###@@@@@@@@@@@
@@@@@@@@@@@##°.#@@#OO@*.*#@##@@@@@@@@######@@@@@@@@##@#*.o@OO#@@#.°##@@@@@@@@@@@
@@@@@@@@@@### *@@#@@Oo##°.o@@##@@@###@@@@@@###@@@##@@o.°##oO@@#@@* ###@@@@@@@@@@
@@@@@@@@@@@##O°°O@##@#oo#O°.O@@###@@@Oo**oO@@@###@@O.°O#oo#@##@o°°O##@@@@@@@@@@@
@@@@@@@@@@@@@@@o°°o#O#@O*O#o.°#@@@#o***oo***o#@@@#°.o#O*O@#O#o°°o@@@@@@@@@@@@@@@
@@@@@@@@@@@@@##@@o°°oOO##ooO#*.*O***o*.  .*o***O*.*#Ooo##OOo°°o@@##@@@@@@@@@@@@@
@@@@@@@@@@@@@@@##@@O°°*oO#OOoOO° **.        .** °OOoO##Oo*°°O@@##@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@##@@O°°*ooO@o*OO.    ....    .OO*o@Ooo*°°O@@##@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@###@@@* °***Oo°°..oO######Oo..°°oO***° *@@@###@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@###@@@O***o° .*°*  .°O@@@@@@@@#*.  *°*. °o***O@@@###@@@@@@@@@@@@@@
@@@@@@@@@@@###@@@Oo****°     . *#*..o###@##O°.*#* .     °****oO@@@###@@@@@@@@@@@
@@@@@@@@@@@@@@#o***o°.        *@@#o.°O####O*.*#@@*        .°o***o#@@@@@@@@@@@@@@
@@@@@@@@@@##O*°*o*.           ###@O°.o####o.°O@###           .*o*°*O##@@@@@@@@@@
@@@@@@@@##O° o#*             .#@##O*.o####o.*O##@#.             *#o °O##@@@@@@@@
@@@@@@@@@@##O*°*o*.           ###@O°.o####o.°O@###           .*o*°*O##@@@@@@@@@@
@@@@@@@@@@@@@@#o***o°.        *@@#o.°O####O°.o#@@*        .°o***o#@@@@@@@@@@@@@@
@@@@@@@@@@@###@@@Oo****°.      *#o.°o######o..o#*      .°****oO@@@###@@@@@@@@@@@
@@@@@@@@@@@@@@###@@@Oo****°  °o ..*O@@@@@@@#o°.  o°  °****oO@@@###@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@###@@#Oo°°.*#oo° .oO######O*. °oo#*.°°oO#@@###@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@##@@o.°OOo*°°     ....     °°*oOO°.o@@##@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#@@O..oOo*°°.*o*.        .*o*.°°*oOo..O@@#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@##@#°.o#O*.°o@#o***o*.  .*o***o#@o°.*O#o.°#@##@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@####@@*.*##*.°o@@#@@@#o***oo***o#@@@#@@o°.*##*.*@@####@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@O.°#@o.°O@@##@###@@@Oo**oO@@@###@##@@O°.o@#°.O@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#@O**°.O@o.°O@@##@@@@@@###@@@@@@###@@@@@@##@@O°.o@O.°**O@#@@@@@@@@@@@
@@@@@@@@@@### *Oo#O.°O@@##@@@@@@@@@@@######@@@@@@@@@@@##@@O°.O#oO* ###@@@@@@@@@@
@@@@@@@@@@@##*.O@# o@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@o #@O.*##@@@@@@@@@@@
@@@@@@@@@@@@#@o.°°.###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###.°°.o@#@@@@@@@@@@@@
''')

#To begin, we will ask for their name to give them a personal greeting
name=input("Please enter your name to begin: ")

print("""
Hello, """ + name +"""! 
Welcome to the MLB Team Chooser!

This program will help you choose your new favorite baseball team!

Play Ball!
""")

def Color():
	team_color = input("Which of the following is your favorite color? Blue, Green, Red, Orange: ")
	if team_color.upper() == "GREEN":
		print("You should root for the Oakland Athletics")
	elif team_color.upper() == "RED" or team_color.upper() =="BLUE" or team_color.upper() == "ORANGE":
		print('\n')
		Time()
	else:
		print("You should root for the Tampa Bay Rays")

def Time():
	time_zone = input("To begin, please choose from the following time zones - EST, CST, MST, PST, Other: ")
	if time_zone.upper() == "EST" or time_zone.upper() == "CST" or time_zone.upper() == "PST":
		print('\n')
		Mascot()
	elif time_zone.upper() == "CST":
		print('\n')
		print("You should root for the Colorado Rockies")
	else:
		print('\n')
		print("You should root for the Texas Rangers")

def Mascot():
	team_mascot = input ("Would you want your new favorite team to have a mascot? Yes or No: ")
	if team_mascot.upper() == "YES":
		print('\n')
		Food()
	else:
		print('\n')
		print("You should root for the Los Angeles Angels of Anaheim")
		
def Food():
	ballpark_food = input("Which of the following ballpark foods is your favorite? Hot dogs, Peanuts, or Cracker Jack: ")
	if ballpark_food.upper() == 'HOT DOG' or ballpark_food.upper() == 'HOTDOG' or ballpark_food.upper() == 'HOT DOGS' or ballpark_food.upper() == 'HOTDOGS' or ballpark_food.upper() =='CRACKER JACKS' or ballpark_food.upper() == 'CRACKERJACKS':
		print('\n')
		History()
	else:
		print('\n')
		print("You should root for the Chicago Cubs")
		
def History():
	team_history = input("Does team history matter to you? Yes or No: ")
	if team_history.upper() == "YES":
		print('\n')
		print("You should root for the New York Mets")
	else:
		print("You should root for the Houston Astros")

def start():
	Start = input("Would you like to begin? Type yes to begin: ")

	if Start.upper() == "YES":
		Color()
	else:
		print("Okay, come back when you're ready. Have a great day!")
		start()

#start()
