import random
import os

def main():
	print("################# Dice Rolling Simulator #################")
	roll = "y"
	while roll == 'y' or roll == 'Y':
		print("We will need you to put the minimum and maximum value and we will get a random number between those.")
		print(random.randint(int(input("Minimum: ")), int(input("Maximum: "))))
		roll = input("Do you want to role the dice again [y/n] ?")
		os.system('cls || clear')
main()
