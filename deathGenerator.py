# Happy pi day everyone!

from random import randint

players = [
'Joe',
'Angus',
'Paul',
'Andreea',
'Simon',
'James'
]

jobs = [
'whore',
'rabbit',
'priest',
'begger',
'milk maid'
]

village='Lovely Burgh'

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

	sadWords = ["Sadly, ","A terrible tragedy occured last night in " +village+".  ", "Bad news.  ", "The village of " +village+" is in mourning today.  ","Sad times.  ", village + " is in despair. "]
	happyWords = ["You'll all be glad to hear that ", "Good news!  ", "After many years of waiting for "+him+" to die, ", "Party in " +village+ " today!  ", village + " can finally celebrate! "]
	neutralWords = ["Curious happenings last night.  ","","By the way, ","","This morning, you were all woken by a loud scream, as ", "While you were all sleeping, ", "Despite your efforts to rid "+village+" of werewolves"]
	sentimentWords=[sadWords,neutralWords,happyWords]

	locationWords = ["in a skip", "at the bottom of the well", "in "+his+" garden", "in "+his+" bed","in the wine cellar","in "+his+" private bed at the village brothel","behind a hedge","under a bush","outside "+randomEntry(players)+"'s house"]

	causesOfDeath = ["mauled to death","ripped to shreds","with "+his+" internal organs scattered everywhere","lying in a pool of blood","with "+his+" ears ripped off","torn from limb to limb","drowned in a barrel of wine"]

	lastWords = ["I leave all my money to my cat.","Tell my wife I cheated on her with a slut.  It was fun.  YOLO.","I had a good life.  Until I was killed, anyway.","Bye!","They're coming for you too.","Don't trust "+randomEntry(players),"I only wish I had confessed my love to "+randomEntry(players)]

	willTypes = [he.capitalize()+" held a note in "+his+" hand.","There was a message scrawled beside "+him+" in blood.","You found "+his+" final tweet."]

	jobDescription = ["the favourite ", "the best ", "the cutest", "the despicable ", "the sexy ", "the adorable "]
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
	job = randomEntry(jobs)
	description = randomEntry(jobDescription)
	occupation = ", " + description + job + ", "
	cause=randomEntry(causesOfDeath)
	words=randomEntry(lastWords)
	willType = randomEntry(willTypes)
	will = willType+'  It read: "'+words+'"'
	return sentimentPrefix+found+" found "+("poor " if randint(0,1)==0 and sentiment==0 else "") + name +(occupation if randint (0,2)==0 else " ")+ location+', '+cause+'.  ' + (will if randint(0,5)==0 else "")


def randomEntry(array):
	return array[randint(0,len(array)-1)]


print deathGenerator("Joe",'M')

