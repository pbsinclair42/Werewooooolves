from deathGenerator import deathGenerator
import os
import platform
import time
import sys

# Clear the screen differently for different operating systems
def clear():
	# Worst case scenario, just make a load of new lines so it looks like the screen has been cleared
	for i in range(0,100):
		print
	if (platform.system()=='Windows'):
		os.system('cls')
	elif (platform.system()=='Linux') or (platform.system()=='Darwin'):
		os.system('clear')

# Display welcome message:
clear()
print "Welcome to Werewolf Helper Deluxe!"
print
# Get the list of players and their professions:
print "Enter the names and professions of all of those in your village, separating the two with a comma, for example 'Joe, narrator' then enter 'end' to end."
players=[]
jobs=[]
inputtedPlayer = raw_input().strip().capitalize()
while (inputtedPlayer!='End'):
	if inputtedPlayer!='Back' and inputtedPlayer!='': # Back is an invalid input, as is <blank>
		if not(',' in inputtedPlayer): # there needs to be a comma separating the name and the job
			print "Invalid input"
		else:
			# Retrieve and save the name and the job:
			name = inputtedPlayer[0:inputtedPlayer.index(',')]
			job = inputtedPlayer[inputtedPlayer.index(',')+1:]
			name = name.strip()
			job=job.strip()
			if (',' in job) or name=='' or job=='' or name=='Back': # Back is an invalid name, no commas are allowed in the name or job, and neither name nor job can be blank
				print "Invalid input"
			elif (name in players): # no duplicate names are allowed
				print name + " is already in the village!  "
			else:
				players.insert(0,name)
				jobs.insert(0,job)
	inputtedPlayer = raw_input().strip().capitalize()

# Get the name of the village:
village = raw_input("Enter the name of your village: ").strip().capitalize()
while village=='':
	village = raw_input("Enter the name of your village: ").strip().capitalize()

print "Great, we're ready to go!"
time.sleep(2)

# Initialize variables:
lastDeath=None
lastDeathJob=None
gameContinues=True

# Main loop:
def menu():
	while gameContinues:
		# Display the options:
		clear()
		print "Pick an option:"
		print
		print "1 - Have a character killed by werewolves.  We'll generate a lovely death message for you!"
		print "2 - Have a character lynched by the village."
		print "3 - Undo the last kill."
		print "4 - View/edit the village."
		print "5 - Announce a winner and end the game!"
		print "6 - See an example message"
		
		toContinue=True

		# Get the option from the user:
		while toContinue:
			selection = raw_input().strip()
			toContinue=False

			# If they wish to have the werewolves kill a character:
			if selection=='1':
				if len(players)<2: # you can't kill the final player
					clear()
					print "There's not enough people left to kill!"
					print
					raw_input('Press Enter to continue...')
				else:
					kill()

			# If they wish to have the village lynch a character:
			elif selection=='2':
				if len(players)<2: # you can't kill the final player
					clear()
					print "There's not enough people left to kill!"
					print
					raw_input('Press Enter to continue...')
				else:
					lynch()

			# If they wish to undo the last kill:
			elif selection=='3':
				undo()

			# If they wish to view/edit the village:
			elif selection=='4':
				edit()

			# If they wish to end the game:
			elif selection=='5':
				end()

			# If they wish to see a sample death message:
			elif selection=='6':
				example()

			# If they done messed up:
			else:
				print "Invalid input, try again."
				toContinue=True


# Kill a character and display a generated death message
def kill():
	clear()
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		# Get the name of the player to be killed
		theDoomedOne = raw_input("Who is getting slaughtered tonight? ").strip().capitalize()
		if (theDoomedOne=='Back'):
			toContinue=False
			clear()
		elif(theDoomedOne==''):
			pass
		elif not (theDoomedOne in players):
			print "Error: "+theDoomedOne + " isn't in the village, or is already dead."
			print "(Current village: "+', '.join(players) + ")"
		else:
			while toContinue:
				# Get the gender of the player to be killed, then kill them
				gender = raw_input("Is "+theDoomedOne+" 1: Male, 2: Female, or 3: Neutral? ").strip()
				if gender=='1' or gender.capitalize()=='Male':
					doTheDeed(theDoomedOne,'M')
					toContinue=False
				elif gender=='2' or gender.capitalize()=='Female':
					doTheDeed(theDoomedOne,'F')
					toContinue=False
				elif gender=='3' or gender.capitalize()=='Neutral':
					doTheDeed(theDoomedOne,'N')
					toContinue=False
				else:
					print 'Invalid input'


# Kill a character and display a generic death message
def lynch():
	clear()
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		# Get the name of the player to be lynched:
		theDoomedOne = raw_input("Who is getting lynched today? ").strip().capitalize()
		if (theDoomedOne == 'Back'): # what a line
			toContinue=False
			clear()
		elif(theDoomedOne==''):
			pass
		elif not (theDoomedOne in players):
			print "Error: "+theDoomedOne + " isn't in the village, or is already dead."
			print "(Current village: "+', '.join(players) + ")"
		else:
			# Lynch the player:
			toContinue=False
			clear()
			print theDoomedOne+' has been lynched!'
			global lastDeathJob
			lastDeathJob = jobs.pop(players.index(theDoomedOne))
			players.remove(theDoomedOne)
			print
			raw_input('Press Enter to continue...')
			global lastDeath
			lastDeath=theDoomedOne


def undo():
	clear()
	global lastDeath
	# If noone has died yet:
	if lastDeath==None:
		print "Noone has died yet!"
		print
		raw_input('Press Enter to continue...')
	# If the last to be killed has already been brought back:
	elif lastDeath=='Back':
		print "You already brought the last person back from the dead!  To bring another person back, edit the village manually."
		print
		raw_input('Press Enter to continue...')
	# If you actually can bring a player back from the dead:
	else:
		print "(Type 'back' to go back to the main menu)"
		print
		print "This will bring "+lastDeath+" back from the dead.  Are you sure you wish to do this?"
		toContinue=True
		while toContinue:
			# Confirm whether to bring back the player 
			answer = raw_input("Y/N: ").strip().capitalize()
			# If yes, bring them back
			if (answer=='Y'):
				print
				print lastDeath+"'s alive!"
				players.insert(0,lastDeath)
				jobs.insert(0,lastDeathJob)
				lastDeath='Back' #Back is being used similarly to None, but for when there was once a death.  This is safe as Back cannot be an actual name.
				toContinue=False
				print
				raw_input('Press Enter to continue...')
			# If no, just head back to the main menu
			elif (answer=='N' or answer=='Back'):
				toContinue=False


def edit():
	global village
	global players
	toContinue=True
	while toContinue:
		# Display the list all players in the village and menu of options
		clear()
		print village+' - Population '+str(len(players))
		print
		for i in range(0,len(players)):
			print players[i]+', '+jobs[i]
		print
		print "Pick an option:"
		print
		print "1 - Add a player"
		print "2 - Remove a player"
		print "3 - Change village name"
		print "4 - Return to main menu"
		
		# Get an option from the user
		toContinue2=True
		while toContinue2:
			toContinue2=False
			selection = raw_input().strip()

			# If adding a player:
			if selection=='1':
				toContinue=True
				while toContinue:
					# Get the new player's name:
					name = raw_input("Enter the new player's name: ").strip().capitalize()
					while name=='':
						name = raw_input("Enter the new player's name: ").strip().capitalize()
					if name=='Back':
						toContinue=False
					elif name!='' and not(','in name):
						if (name in players):
							print name + " is already in the village!  "
						else:
							# Add the name
							players.insert(0,name)
							# Get the player's job:
							job = raw_input("Enter "+name+"'s profession: ").strip()
							while job=='' or (',' in job):
								job = raw_input("Enter "+name+"'s profession: ").strip()
							jobs.insert(0,job)
							toContinue=False
				toContinue=True

			# If removing a player:
			elif selection=='2':
				toContinue=True
				while toContinue:
					# Get the player to remove's name:
					name = raw_input("Enter the name of the player to remove: ").strip().capitalize()
					while name=='':
						name = raw_input("Enter the name of the player to remove: ").strip().capitalize()
					if name=='Back':
						toContinue=False
					elif not (name in players):
						print name + " is not currently in the village!  "
					else:
						# Remove that player
						job = jobs.pop(players.index(name))
						players.remove(name)
						toContinue=False
				toContinue=True

			# If changing the name of the village:
			elif selection=='3':
				# Get the new village name
				village = raw_input("Enter the new village name: ").strip().capitalize()
				while village=='':
					village = raw_input("Enter the new village name: ").strip().capitalize()

			# If going back to the main menu:
			elif selection=='4' or selection.capitalize()=='Back':
				toContinue=False

			# If they done messed up:
			else:
				print "Invalid input, try again."
				toContinue2=True


def end():
	global gameContinues
	clear()
	print "(Type 'back' to go back to the main menu)"
	print
	toContinue=True
	while toContinue:
		# Get the winner:
		winners = raw_input("Good game!  Who won, 1: Werewolves or 2: Villagers? ").strip()

		# If werewolves won:
		if(winners=='1' or winners.capitalize()=="Werewolves"):
			clear()
			print "Arrroooooooooooooooooooo!"
			toContinue=False
			gameContinues=False # end the game
			print
			raw_input('(Press Enter to exit)')

		# If the villagers won:
		elif (winners=='2' or winners.capitalize()=='Villagers'):
			clear()
			print "Hurrah!  "+village+" is safe once more!"
			toContinue=False
			gameContinues=False # end the game
			print
			raw_input('(Press Enter to exit)')

		# If going back to the main menu:
		elif (winners.capitalize()=='Back'):
			toContinue=False

		#If they done messed up:
		else:
			print "Invalid input"


def example():
	clear()
	print "Example death message:"
	print
	# Display a death message without impacting the state of the game by providing some dummy parameters:
	print deathGenerator('Joe','M','provider of happiness',['Angus','Paul','Andreea','James'],'HackTheBurgh')
	print
	raw_input('Press Enter to continue...')

# Have the werewolves kill off a player:
def doTheDeed(theDoomedOne,gender):
	# Remove the player:
	clear()
	job = jobs.pop(players.index(theDoomedOne))
	players.remove(theDoomedOne) # the best line of code I have ever written
	print deathGenerator(theDoomedOne,gender,job,players,village) # display the death message
	print
	raw_input('Press Enter to continue...')
	# Save the last death
	global lastDeath
	global lastDeathJob
	lastDeath=theDoomedOne
	lastDeathJob=job

menu()

