from deathGenerator import deathGenerator
import os
import time

print "Welcome to Werewolf Helper!"
print "Enter the names of all of those in your village, then 'end' to end."
players=[]
name = raw_input()
name = name.capitalize()
while (name!='End'):
	if name!='Back':
		if (name in players):
			print name + " is already in the village!  "
		else:
			players.insert(0,name)
	name = raw_input()

village = raw_input("Enter the name of your village: ")

print "Great, we're ready to go!"
time.sleep(2)

lastDeath=None


def menu():
	while True:
		os.system('cls')
		print "Pick an option:"
		print
		print "1 - Have a character killed by werewolves.  We'll generate a lovely death message for you!"
		print "2 - Have a character lynched by the village."
		print "3 - Undo the last kill."
		print "4 - View/edit the village."
		print "5 - Announce a winner and end the game!"
		print "6 - See an example message"
		
		toContinue=True

		while toContinue:
			selection = raw_input()
			toContinue=False
			if selection=='1':
				kill()
			elif selection=='2':
				lynch()
			elif selection=='3':
				undo()
			elif selection=='4':
				edit()
			elif selection=='5':
				end()
			elif selection=='6':
				example()
			else:
				print "Invalid input, try again."
				toContinue=True


def kill():
	os.system('cls')
	print "(Type 'back' to go back to the main menu)"
	toContinue=True
	while toContinue:
		theDoomedOne = raw_input("Who is getting slaughtered tonight? ").capitalize()
		if (theDoomedOne=='Back'):
			toContinue=False
			os.system('cls')
		elif not (theDoomedOne in players):
			print "Error: "+theDoomedOne + " isn't in the village, or is already dead."
			print "(Current village: "+', '.join(players) + ")"
		else:
			while toContinue:
				gender = raw_input("Is "+theDoomedOne+" 1: Male, 2: Female, or 3: Neutral? ")
				if gender=='1' or gender.capitalize=='Male':
					doTheDeed(theDoomedOne,'M')
					toContinue=False
				elif gender=='2' or gender.capitalize=='Female':
					doTheDeed(theDoomedOne,'F')
					toContinue=False
				elif gender=='3' or gender.capitalize=='Neutral':
					doTheDeed(theDoomedOne,'N')
					toContinue=False
				else:
					print 'Invalid input'


def doTheDeed(theDoomedOne,gender):
	os.system('cls')
	print deathGenerator(theDoomedOne,gender)
	players.remove(theDoomedOne)
	print
	raw_input('Press Enter to continue...')

menu()

