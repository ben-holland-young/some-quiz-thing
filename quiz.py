
import random

#Get the users playerName
playerName = input("What would you like your player name to be?\n")


#Demo/example question
print("This is how you play the game")
print("You will be asked a question like this")
print("Question 1 --- When was Python created?")
print("A - 1980")
print("B - 1950")
print("C - 2001")
print("You would then input your answer(A,B or C), and your score would be incremented by 10 if you win. If you lose a score of 0 is given.")
print("So if you got two questions right on a level you'd get 10/20")


#Prompt to begin
begin = input("Ready to begin? y/n\n")
begin.lower()
if begin == "y":
	print("Let's go")
elif begin == "n":
	print("Bye i guess")
	exit()
else:
	print("Not recognised")
	
	
#Could use a dictionary but typos could occur because of the use of a key which would the question compared to indexes used in arrays or a multidimensional array in this case
level1 = [["What is CEOP?", "Child Exploitation and Online Protection", "Criminal Exploration and Online Protection", "Child Exploitation and Organised Protectors"]]
level2 = [["When you get an email from someone you do not know, what should you do?", "Delete it and mark as spam", "Reply and say hello", "Forward to your friends"]]
level3 = [["How secret should you keep your passwords?", "Never give out passwords except to your parents", "Give them only to your best friends", "Give them to strangers"]]
level4 = [["When an online contact who frightens you asks to meet you in person what should you do?", "Report to CEOP", "Arrange to meet them", "Arrange to meet them with your best friend"]]
level5 = [["If an email asks you to enter your bank account details because of a problem with your account what should you do?", "Contact the bank to check if they sent the email", "Reply to the email", "Enter your bank account details"]]

globalLevels = [level1, level2, level3, level4, level5]
#Global Score levels
scoreLevel = []
totalScore = 0


def questions(level, scoreLevel, level_number):
	print("Starting Level %d, the current score is 0" % level_number)
	#Using a for loop to go through questions
	for x in level:
		
		score = 0
		#This generates the question number in the level
		questionIndex = random.randint(0,len(level) -1)
		print(questionIndex)
		
		#Ask question have a
		print(level[questionIndex][0])
		#Printing Options
		print("A - " + level[questionIndex][1])
		print("B - " + level[questionIndex][2])
		print("C - " + level[questionIndex][3])
		#Getting the answer. 
		answer = input("\n")
		answer = answer.capitalize()
		if answer == "A":
			print("You got it right, ten points to " + playerName)
			print("------------------------------------")
			score = 20
			
		elif  answer == "B" or  answer == "C":
			print("You got it wrong, no score :(")
			score = 0
			
		else:
			print("Unrecognised answer...qutting")
					
		
		scoreLevel.append(score)
		#totalScore = totalScore + score
		print("You got " + str(scoreLevel) + "/20 points on Level %d." % level_number)
		print("------------------------------------")
	
for x in range(0, len(globalLevels)-1):
	randomLevel = random.randint(0, len(globalLevels)-1)
		
	questions(globalLevels[randomLevel] ,scoreLevel , x)


#Ending The game
for x in range(0,4):
	print(playerName +  " on level " + str((x+1)) + " you got " + str(scoreLevel[x]) + ". You got a 	total of " + str(totalScore))

print("Thanks for playing the game, " + playerName)
		

	
	
	
	
	
	
	
	
	
	
	
