
import random

##Get the users playerName
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
#set begin variable to begin.lower
begin = begin.lower()
#control flow over begin variable
if begin == "y":
	print("Let's go")
elif begin == "n":
	print("Bye i guess")
	exit()
else:
	print("Not recognised")

	
#first layer == levels, second, level contents, third , questions using a 3 dimensional array to store questions and answers in levels
levels = [[["What is CEOP?", "Child Exploitation and Online Protection", "Criminal Exploration and Online Protection", "Child Exploitation and Organised Protectors"]], [["When you get an email from someone you do not know, what should you do?", "Delete it and mark as spam", "Reply and say hello", "Forward to your friends"]], [["How secret should you keep your passwords?", "Never give out passwords except to your parents", "Give them only to your best friends", "Give them to strangers"]], [["When an online contact who frightens you asks to meet you in person what should you do?", "Report to CEOP", "Arrange to meet them", "Arrange to meet them with your best friend"]], [["If an email asks you to enter your bank account details because of a problem with your account what should you do?", "Contact the bank to check if they sent the email", "Reply to the email", "Enter your bank account details"]] ] 


#Global variables
#Running score, a running total for the quiz
runningScore = 0
#Currently in development scores array to store level-wise scores
scores = []
#Current--- varaibles, because of my structure i need to keep track of the current data for my question and level
current_level = 0
current_question = ""
current_answerA = ""
current_answerB = ""
current_answerC = ""

#index generation for the level and question
def randomLevelIndex():
	randomLevel = random.randint(0, len(levels) -1)
	
	return randomLevel


def randomQuestionIndex():
	randomQuestion = random.randint(0, len(levels[randomLevelIndex()]) -1)
	
	return randomQuestion

#question generation, basically generates a random question using the other two index producing methods
def returnRandomQuestion():
	global current_question
	global current_answerA
	global current_answerB
	global current_answerC
	randomLevel = levels[randomLevelIndex()]
	current_level = randomLevel
	randomQuestion = randomLevel[randomQuestionIndex()]
	current_question = randomQuestion
	question = randomQuestion[0]
	current_question = question
	current_answerA = randomQuestion[1]
	current_answerB = randomQuestion[2]
	current_answerC = randomQuestion[3]
	return question
	
	
	
#scoring, simple function using the running score variable to increment it on a correct answer.
def incrementScore():
	#use 'global' syntax to use global variables inside functions or loops to avoid conflicts with local variables.
	global runningScore 
	runningScore = runningScore + 20

#verification- checks if the answer is correct and assigns corresponding functions
def checkAnswer(anAnswer):
	if anAnswer == "A":
		score = 20
		incrementScore()
		print("You got it right! Your running score is %s" % runningScore)
		return True
		scores.append(score)
	elif anAnswer == "B" or anAnswer == "C":
		score = 0
		print("You got it wrong! Your running score is %s" % runningScore)
		return False
		scores.append(score)
	else:
		score = 0
		print("Unrecognised answer! Your running score is %s" % runningScore)
		scores.append(score)
	

#ask the questions
def askQuestions():
	#Uses random question function to print the question
	print(returnRandomQuestion())
	#use global current variables to print options using interpolation syntax or formatting a string syntax '%'
	print("A -  %s" % current_answerA)
	print("B -  %s" % current_answerB)
	print("C -  %s" % current_answerC)
	
	#gets input for answer and adds this as an attribute to the 'checkAnswer' method. Then uses a \n escape sequence to get a new line
	answer = input("\n")
	checkAnswer(answer)
	


#Asks question five times (still in development)
for x in range(0,5):
	askQuestions()
	












