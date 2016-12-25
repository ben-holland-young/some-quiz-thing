#Open the text file 
scores = open("scores.txt")


#Get The data out of the text file. 
players = []
for line in scores:
	
	#Here we get the name
	name = []
	level = []
	score = []

#	for x in line:
#		name.append(x)
#		if x == ",":
#			break
#	name.pop()
#	name = ''.join(name)
	stuff = line.split(",")
	name =  stuff[2]
	print(name)
	
	
#	#Here we get the level
#	for x in range(len(name) +1, len(line)):
#		
#		level.append(line[x])
#		
#		if x == ",":
#			break
#		 
#			
#	
#	level = level[0]
#
#	
#	#Here we get the score
#	for x in range(len(level) + len(name) +1, len(line)):
#		
#		score.append(line[x])
#		
#		if line[x] == ' ':
#			score.remove(line[x])
#		if line[x] == "\n":
#			score.remove(line[x])
#		if line[x] == ",":
#			score.remove(line[x])
#		if x == ",":
#			break
#	
#		
#	if len(score) == 2:
#		score = int(score[0] + score[1])
#	else:
#		score = int(score[0])
#		
#	player = [name, level, score]
#	
#	
#	players.append(player)
#level = int(level)
#
##Option 1
#def option1(name):
#	for x in players:
#		#x[0]
#		if x[0] == name:
#			print("The player got the score " + str(x[1]) + " on level " + str(x[2]) )
#			
#			
#			
##Option 2 - highest score per level 
#def option2():
#	highestInLevel_1 = 0
#	highestName_1 = ""
#	level_1 = '1'
#	for x in players:
#		if x[1] == level_1:
#			if x[2] > highestInLevel_1:
#				highestInLevel_1 = x[2]
#				highestName_1 = x[0]
#
#	print("----------------")
#	print("A score of " + str(highestInLevel_1))
#	print("By " + highestName_1)
#	print("In level " + level_1)
#	print("----------------")
#
#
#	highestInLevel_2 = 0
#	highestName_2 = ""
#	level_2 = '2'
#	for x in players:
#		if x[1] == level_2:
#			if x[2] > highestInLevel_2:
#				highestInLevel_2 = x[2]
#				highestName_2 = x[0]
#				
#	print("----------------")
#	print("A score of " + str(highestInLevel_2))
#	print("By " + highestName_2)
#	print("In level " + level_2)
#	print("----------------")	
#
#
#	highestInLevel_3 = 0
#	highestName_3 = ""		
#	level_3 = '3'
#	for x in players:
#		if x[1] == level_3:
#			if x[2] > highestInLevel_3:
#				highestInLevel_3 = x[2]
#				highestName_3 = x[0]
#				
#	print("----------------")
#	print("A score of " + str(highestInLevel_3))
#	print("By " + highestName_3)
#	print("In level " + level_3)
#	print("----------------")
#			
#
#
#	highestInLevel_4 = 0
#	highestName_4 = ""
#	level_4 = '4'
#	for x in players:
#		if x[1] == level_4:
#			if x[2] > highestInLevel_4:
#				highestInLevel_4 = x[2]
#				highestName_4 = x[0]
#
#	print("----------------")
#	print("A score of " + str(highestInLevel_4))
#	print("By " + highestName_4)
#	print("In level " + level_4)
#	print("----------------")
#
#	highestInLevel_5 = 0
#	highestName_5 = ""
#	level_5 = '5'
#	for x in players:
#		if x[1] == level_5:
#			if x[2] > highestInLevel_5:
#				highestInLevel_5 = x[2]
#				highestName_5 = x[0]
#	print("----------------")
#	print("A score of " + str(highestInLevel_5))
#	print("By " + highestName_5)
#	print("In level " + level_5)
#	print("----------------")
#			
#			
#			
##Option 3
##def option3():
#name = ""
#totalScore = 0
#for x in players:
#	#print(x)
#	totalScore = x[2]
#	name = x[0]
#	if x[0] == name:
#		totalScore = totalScore + x[2]
#	print(totalScore)
#	
#print("The person with the highest score is " + name + " with a combined score of " + str(totalScore)
#
#	

	
#Starting scoreboard interface
#print("Welcome to the scoreboad, press the numbers according to the option you want.")
#print("1: Option 1, Scores for a specific player")
#print("2: Option 2, Highest scorer for each level")
#print("3: Option 3, Highest scorer in the game")
#option = input("")

#if option == "1":
#	name = input("Name to search?\n")
#	option1(name)
#elif option == "2":
#	option2()
#elif option == "3":
#	option3()
#else:
#	print("Not recognised, qutting...")
#	
#















	