from deathGenerator import deathGenerator
import os
import time

os.system('cls')
print "Welcome to Werewolf Helper!"
print
print "Enter the names of all of those in your village, then 'end' to end."
players=[]
name = raw_input().capitalize()
while (name!='End'):
	if name!='Back' and name!='':
		if (name in players):
			print name + " is already in the village!  "
		else:
			players.insert(0,name)
	name = raw_input().capitalize()

village = raw_input("Enter the name of your village: ").capitalize()
while village=='':
	village = raw_input("Enter the name of your village: ").capitalize()

print "Great, we're ready to go!"
time.sleep(2)

lastDeath=None
gameContinues=True

def menu():
	while gameContinues:
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
	os.system('cls')


def kill():
	os.system('cls')
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		theDoomedOne = raw_input("Who is getting slaughtered tonight? ").capitalize()
		if (theDoomedOne=='Back'):
			toContinue=False
			os.system('cls')
		elif(theDoomedOne==''):
			pass
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

def lynch():
	os.system('cls')
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		theDoomedOne = raw_input("Who is getting lynched today? ").capitalize()
		if (theDoomedOne=='Back'):
			toContinue=False
			os.system('cls')
		elif(theDoomedOne==''):
			pass
		elif not (theDoomedOne in players):
			print "Error: "+theDoomedOne + " isn't in the village, or is already dead."
			print "(Current village: "+', '.join(players) + ")"
		else:
			toContinue=False
			os.system('cls')
			print theDoomedOne+' has been lynched!'
			players.remove(theDoomedOne)
			print
			raw_input('Press Enter to continue...')
			global lastDeath
			lastDeath=theDoomedOne

def undo():
	os.system('cls')
	print "(Type 'back' to go back to the main menu)"
	print
	global lastDeath
	if lastDeath==None:
		print "Noone has died yet!"
		print
		raw_input('Press Enter to continue...')
	elif lastDeath=='Back':
		print "You already brought the last person back from the dead!  To bring another person back, edit the village manually."
		print
		raw_input('Press Enter to continue...')
	else:
		print "This will bring "+lastDeath+" back from the dead.  Are you sure you wish to do this?"
		toContinue=True
		while toContinue:
			answer = raw_input("Y/N: ").capitalize()
			if (answer=='Y'):
				print
				print lastDeath+"'s alive!"
				players.insert(0,lastDeath)
				lastDeath='Back' #Back is being used similarly to None, but for when there was once a death.  This is safe as Back cannot be an actual name.
				toContinue=False
				print
				raw_input('Press Enter to continue...')
			elif (answer=='N' or answer=='Back'):
				toContinue=False


def edit():
	global village
	global players
	toContinue=True
	while toContinue:
		os.system('cls')
		print village+' - Population '+str(len(players))
		print
		print '\n'.join(players)
		print
		print "Pick an option:"
		print
		print "1 - Add a player"
		print "2 - Remove a player"
		print "3 - Change village name"
		print "4 - Return to main menu"
		
		toContinue2=True
		while toContinue2:
			toContinue2=False
			selection = raw_input()
			if selection=='1':
				toContinue=True
				while toContinue:
					name = raw_input("Enter the new player's name: ").capitalize()
					if name=='Back':
						toContinue=False
					elif name!='':
						if (name in players):
							print name + " is already in the village!  "
						else:
							players.insert(0,name)
							toContinue=False
				toContinue=True
			elif selection=='2':
				toContinue=True
				while toContinue:
					name = raw_input("Enter the name of the player to remove: ").capitalize()
					if name=='Back':
						toContinue=False
					elif not (name in players):
						print name + " is not currently in the village!  "
					else:
						players.remove(name)
						toContinue=False
				toContinue=True
			elif selection=='3':
				village = raw_input("Enter the new village name: ").capitalize()
				while village=='':
					village = raw_input("Enter the new village name: ").capitalize()
			elif selection=='4' or selection.capitalize()=='Back':
				toContinue=False
			else:
				print "Invalid input, try again."
				toContinue2=True

def end():
	global gameContinues
	os.system('cls')
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		winners = raw_input("Good game!  Who won, 1: Werewolves or 2: Villagers? ")
		if(winners=='1' or winners.capitalize()=="Werewolves"):
			print "Arrroooooooooooooooooooo!"
			toContinue=False
			gameContinues=False
			print
			raw_input('(Press Enter to exit)')
		elif (winners=='2' or winners.capitalize()=='Villagers'):
			print "Hurrah!  "+village+" is safe once more!"
			toContinue=False
			gameContinues=False
			print
			raw_input('(Press Enter to exit)')
		elif (winners.capitalize()=='Back'):
			toContinue=False
		else:
			print "Invalid input"

def example():
	os.system('cls')
	print "Example death message:"
	print
	print deathGenerator('Joe','M',['Angus','Paul','Andreea','James'],'HackTheBurgh')
	print
	raw_input('Press Enter to continue...')

def doTheDeed(theDoomedOne,gender):
	os.system('cls')
	players.remove(theDoomedOne)
	print deathGenerator(theDoomedOne,gender,players,village)
	print
	raw_input('Press Enter to continue...')
	global lastDeath
	lastDeath=theDoomedOne

menu()

