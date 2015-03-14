from random import randint

players = [
'Player1',
'Player2',
'Player3'
]

village='Lovely Burgh'

sadWords = ["Sadly, ","A terrible tragedy occured last night" +village+".  ", "Bad news.  ", "The village of " +village+" is in mourning today.  ","Sad times.  ", village + " is in despair. "]
happyWords = ["You'll all be glad to hear that ", "Good news!  ", "After many years of waiting, ", "Party in " +village+ " today!  "]
neutralWords = ["Curious happenings last night.  ","","By the way, ","","This morning, you were all woken by a loud scream, as "]

sentimentWords=[sadWords,neutralWords,happyWords]


def deathGenerator(name,gender):

	if (gender=='M'):
		he='he'
		his='his'
		him='him'
	elif (gender=='F'):
		he='she'
		his='her'
		him='her'
	elif (gender=='N'):
		he='they'
		his='their'
		him='them'
	else:
		return "Invalid gender, enter M, F or N"

	locationWords = ["in a skip", "at the bottom of the well", "in "+his+" garden", "in "+his+" bed","in the wine cellar","in "+his+" private bed at the village brothel"]

	causesOfDeath = ["mauled to death","ripped to shreds","with "+his+" internal organs scattered everywhere","lying in a pool of blood","with "+his+" ears ripped off","torn from limb to limb","hanging from a tree","drowned in a barrel of wine"]

	lastWords = ["I leave all my money to my cat.","Tell my wife I cheated on her with a slut.  It was fun.  YOLO.","I had a good life.  Until I was killed, anyway","Bye!"]

	willTypes = [he.capitalize()+" held a note in "+his+" hand.","There was a message scrawled beside "+him+" in blood.","You find "+his+" final tweet."]

	found = players[randint(0,len(players)-1)]
	sentiment = randint(0,10) # 1/10 chance of happy, 6/10 chance of sad, 3/10 chance of neutral
	if (sentiment==0):
		sentiment=2 # happy
	elif (sentiment<4):
		sentiment=1 # neutral
	else:
		sentiment=0 # sad

	sentimentPrefix = randomEntry(sentimentWords[sentiment]) 
	location = randomEntry(locationWords)
	cause=randomEntry(causesOfDeath)
	words=randomEntry(lastWords)
	willType = randomEntry(willTypes)
	will = willType+'  It read: "'+words+'"'
	return sentimentPrefix+found+" found " + name +" "+ location+', '+cause+'.  ' + (will if randint(0,5)==0 else "")

def randomEntry(array):
	return array[randint(0,len(array)-1)]


print deathGenerator("Bob",'M')








#"over there.  And over there.  And over there.  ...and over there"