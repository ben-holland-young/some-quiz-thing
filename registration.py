#Welcome message
print("Welcome to the quiz")

infoCorrect = True
while infoCorrect: 
    #Getting age and using an if statement to make it pretty
    age = int(input("How old are you?"))
    if age >= 12:
        print("Welcome to the game")
    else:
        #Exiting because not meeting the requirement
        print("You're too young")
        exit()

    #Using a while loop to verify and set gender
    condition = True
    while condition:
        gender = input("Are you 1: male, 2: female, 3: non conforming")
        if gender == "1":
            gender = "male"
            condition = False
        elif gender == "2":
            gender = "female"
            condition = False
        elif gender == "3":
            gender = "non-conforming"
            condition = False
        else:
            print("Not recognised...qutiing")
            exit()

    #Get email. 
    email = input("What is your email?")
    #Get Player name
    playerName = input("What will your player name be?")


    #Display all variables
    print("Your name is " + playerName)
    print("Your age is " + str(age))
    print("Your gender is " + gender)
    print("Your email address is " + email)


    #Ask user if the info displayed is correct.
    correct = input("y/n")
    if correct == "y":
        print("We shall continue")
        infoCorrect = false
        exit()
    else:
        print("Selection not recognised, quitting.")
        
