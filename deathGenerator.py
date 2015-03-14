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

locationWords = ["in a skip", "at the bottom of the well", "over there.  And over there.  And over there.  ...and over there", "in their garden", "in their bed","in the wine cellar","in his private bed at the village brothel"]

causesOfDeath = []

def deathGenerator(name):
	found = players[randint(0,len(players)-1)]
	sentiment = randint(0,2) #0 is sad, 1 is neutral, 2 is happy
	sentimentPrefix = sentimentWords[sentiment][randint(0,len(sentimentWords[sentiment])-1)]
	location = locationWords[randint(0,len(locationWords)-1)]
	cause=""
	return sentimentPrefix+found+" found " + name +" "+cause + location



print deathGenerator("Bob")
