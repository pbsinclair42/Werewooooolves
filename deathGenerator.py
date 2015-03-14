from random import randint

players = [
'Player1',
'Player2',
'Player3'
]

sadWords = ["Sadly, ","A terrible tragedy occured last night.  ", "Bad news.  ", "The village is in mourning today.  "]
happyWords = ["Fortunately, ", "Good news!  ", "After many years of waiting, ", "Party in the village today!  "]
neutralWords = ["By the way, ",""]
sentimentWords=[sadWords,neutralWords,happyWords]

locationWords = ["in a skip", "at the bottom of the well", "in their garden", "in their bed","in the wine cellar","in his private bed at the village brothel"]

causesOfDeath = ["mauled to death","ripped to shreds","with their internal organs scattered everywhere","lying in a pool of blood","with its ears ripped off","torn from limb to limb","hanging from a tree","drowned in a barrel of wine"]

lastWords = ["I leave all my money to my cat.","Tell my wife I cheated on her with a slut.  It was fun.  YOLO.","I had a good life.  Until I was killed, anyway"]

def deathGenerator(name):
	found = players[randint(0,len(players)-1)]
	sentiment = randint(0,2) #0 is sad, 1 is neutral, 2 is happy
	sentimentPrefix = sentimentWords[sentiment][randint(0,len(sentimentWords[sentiment])-1)]
	location = locationWords[randint(0,len(locationWords)-1)]
	cause=causesOfDeath[randint(0,len(causesOfDeath)-1)]
	will=lastWords[randint(0,len(lastWords)-1)]
	return sentimentPrefix+found+" found " + name +" "+cause + " "+ location+'.  They held a note in their hand.  It read: "'+will+'"'



print deathGenerator("Bob")








#"over there.  And over there.  And over there.  ...and over there"