import random
import re
scores = open("scores.txt")
players = []
for line in scores:
	#Player array - name level score
	player = line.split(",")
	
	
	#Do check on data
	#Score:
	#Using .re to replace not needed characters
	player[2] = re.sub("\n", '',player[2])
	#Typecasting to an integer
	player[2] = int(re.sub(" ", '', player[2]))
	#Checking size
	if player[2] < 0:
		player[2] = 1
	#Level:
	#Typecasting to an integer
	player[1] = int(player[1])
	if player[1] < 1 or player[1] > 6:
		player[1] = 1
	
	#Append player array to players after checks
	players.append(player)
	
	
	
	
	
def option1(name):
	for x in players:
		#print(x)
		if x[0] == name:
			print("Got it")
			print("%s got the score %d on level %d" % (x[0], x[1], x[2] ))
			if 
		else:
			print("Not found")
option1("Starplayer")