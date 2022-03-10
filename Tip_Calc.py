#!/usr/bin/python

print('Welcome to the tip calculator! \n')

#Create variable asking for price of bill
bill = float(input('What is the total price of your bill? \n'))

#Create variable asking for tip percentage
tip = float(input('What % would you like to tip? \n'))

#Create variable asking how many people are splitting the bill
people = int(input('How many people are splitting this bill? \n'))
print("\n")

#Calculate the tip
gratuity = (round(float(tip /100) * float(bill),2))

#Calculate total amount
total = (round(float(gratuity) + float(bill),2))

#Calculate amount each person owes
split = (round(float(total) / float(people), 2))

#Show the results
print("Your tip is $"+ str(gratuity))
print("Your total bill is $"+ str(total))
print("Each person owes $" + str(split) +'\n')
print("Thank you for using the tip calculator. Enjoy the rest of your day!")
