import re
scores = open("scores.txt")
for line in scores:
        print(line)
        split = line.split(",")
        name = split[0]
        level = int(split[1])
        if level < 0 or level == 0:
            level = 1
	score = int
	
