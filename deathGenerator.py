# Happy pi day everyone!

from random import randint

jobs = [
'whore',
'rabbit',
'priest',
'beggar',
'milk maid'
]


def deathGenerator(name,gender,job,players,village):

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


	sadWords = ["Sadly, ", "A terrible tragedy occured last night in " +village+".  ", "Bad news.  ", "The village of " +village+" is in mourning today.  ","Sad times.  ", village + " is in despair. "]
	
	happyWords = ["You'll all be glad to hear that ", "Finally!  ", "There is one villager less in "+village+".  ", "Hey everyone, guess what happened last night!  ", "Good news!  ", "After many years of waiting for "+him+" to die, ", "Party in " +village+ " today!  ", village + " can finally celebrate! "]
	
	neutralWords = ["Curious happenings last night.  ", "In case you didin't notice, ","","This morning, you were all woken by a loud scream, as ", "While you were all sleeping, ", "Despite your efforts to rid "+village+" of werewolves, "]
	
	sentimentWords=[sadWords,neutralWords,happyWords]

	locationWords = ["in a skip", "at the bottom of the well", "in "+his+" garden", "in "+his+" bed","in the wine cellar","in "+his+" private bed at the village brothel","behind a hedge","under a bush","outside "+randomEntry(players)+"'s house", "in the fields","in the stables","under the bridge"]

	causesOfDeath = [", mauled to death", ", ripped to shreds",", with "+his+" internal organs scattered everywhere",", lying in a pool of blood",", with "+his+" ears ripped off",", torn from limb to limb",", drowned in a barrel of wine",", with "+his+" heart ripped from his chest - and not metaphorically either",", though "+his+" head was found at the other end of "+village,", looking like "+he+"'d been chewed up and spat out again", ", drowned in "+his+" own blood",", with one less face then normal",", looking even more dead than usual",".  There were clear signs of a struggle all around, and clearly "+name+" had not come off well"]

	lastWords = ["I will come back and haunt you!","You're just a bunch of useless old villagers!" ,"I hope you're all happy now!","I leave all my money to my cat.","Tell my wife I cheated on her with a slut.  It was fun.  YOLO.","Ow.","Bye!","They're coming for you too.","Don't trust "+randomEntry(players),"I only wish I had confessed my love to "+randomEntry(players),"Beware, "+randomEntry(players)+" - you're next."]

	willTypes = [he.capitalize()+" held a note in "+his+" hand.  It read: ","There was a message scrawled beside "+him+" in blood.  It read: ","You found "+his+" final tweet.  It read: ","You hear +"+his+" dying words: ","As "+he+" was killed, "+he+" yelled "]


	sadJobs = [village+"'s favourite ", village+"'s best ", "the sexy ","the much loved ", "the adorable "]
	neutralJobs = ["the "]
	happyJobs = [ "the despicable ","the evil ", "everyone's least favourite "]
	jobDescription = [sadJobs,neutralJobs,happyJobs]

	findingWords = [" stumbled upon the dead body of ", " found what appeared to be ", " set eyes on the dead body of ", " ran into the remains of "]

	found = randomEntry(players)

	circumstancesWords = ["While doing the laundry, ", "While picking carrots, ", "While taking a morning walk, ", "While tending to the sheep, ", "On the way to fetch some water, ", "While taking part in some perfectly ordinary daily business, "]
	
	sentiment = randint(0,10) # 1/10 chance of happy, 6/10 chance of sad, 3/10 chance of neutral
	if (sentiment==0 or name=="Joe"):
		sentiment=2 # happy
	elif (sentiment<4):
		sentiment=1 # neutral
	else:
		sentiment=0 # sad

	findingWay = randomEntry(findingWords)
	sentimentPrefix = randomEntry(sentimentWords[sentiment]) 
	location = randomEntry(locationWords)
	description = randomEntry(jobDescription[sentiment])
	occupation = ", " + description + job 
	cause=randomEntry(causesOfDeath)
	words=randomEntry(lastWords)
	circumstances = randomEntry(circumstancesWords)
	willType = randomEntry(willTypes)
	will = willType+'"'+words+'"'

	randomstory=randint(0,1);
	if(randomstory == 0):
		return sentimentPrefix+ found+ findingWay +("poor " if randint(0,1)==0 and sentiment==0 else "") + name +(occupation if randint (0,1)==0 else "")+ (", "+location if randint(0,1)==0 else "")+cause+'.  ' + (will if randint(0,5)==0 else "")
	elif(randomstory == 1):
		return circumstances + found + findingWay + name + (occupation if randint(0,1)==0 else "") + (", "+location if randint(0,1)==0 else "") +cause +'.  '+ (will if randint(0,3)==0 else "")

def randomEntry(array):
	return array[randint(0,len(array)-1)]


# ~(34,137,600 * number of players) different messages available, for any fixed name, gender, job, players and village