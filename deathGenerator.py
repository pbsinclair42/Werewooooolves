from random import randint

players = [
'Player1',
'Player2',
'Player3'
]

sadWords = ["Sadly, ","A terrible tragedy occured last night.  ", "Bad news.  ", "The village is in mourning today.  "]
happyWords = ["You'll all be glad to hear that ", "Good news!  ", "After many years of waiting, ", "Party in the village today!  "]
neutralWords = ["By the way, ",""]
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
	else:
		return "Invalid gender, enter M or F"

	locationWords = ["in a skip", "at the bottom of the well", "in "+his+" garden", "in "+his+" bed","in the wine cellar","in "+his+" private bed at the village brothel"]

	causesOfDeath = ["mauled to death","ripped to shreds","with "+his+" internal organs scattered everywhere","lying in a pool of blood","with "+his+" ears ripped off","torn from limb to limb","hanging from a tree","drowned in a barrel of wine"]

	lastWords = ["I leave all my money to my cat.","Tell my wife I cheated on her with a slut.  It was fun.  YOLO.","I had a good life.  Until I was killed, anyway","Bye!"]

	willTypes = [he.capitalize()+" held a note in "+his+" hand.","There was a message scrawled beside "+him+" in blood.","You find "+his+" final tweet."]

	found = players[randint(0,len(players)-1)]
	sentiment = randint(0,2) #0 is sad, 1 is neutral, 2 is happy
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