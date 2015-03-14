
print "Welcome to Werewolf Helper!"
print "Enter the names of all of those in your village, then 'end' to end."
names=[]
name = raw_input()
while (name!='end'):
	names.insert(0,name)
	name = raw_input()


print "Enter the name of your village:"
village = raw_input()

print "Great, we're ready to go!"
displayMenu()

def displayMenu():
	print "Pick an option:"
	print "1 - Have a character killed by werewolves.  We'll generate a lovely death message for you!"
	print "2 - Have a character lynched by the village."
	print "3 - Edit the village."
	print "4 - Announce a winner!"
	print "5 - See an example message"