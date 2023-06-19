import random # Import random libarary

print("\n----------------------------WELCOME TO THE Snake Water Gun (SWG) GAME----------------------------")
print("-------------------------------------------------------------------------------------------------\n")
choice = int(input("Enter the game mode:\n1)With two Player:\n2)With Computer:\t"))# This asking for game mode

#FUNCTION WORK WHEN GAME BETWEEN ANY USER AUR COMPUTER
def PointOfComputerAndPlayer(user,computer):
    if(user == computer):
        return 0 #When Both Inputs are equal
    elif(computer == 0 and user == 1 or computer == 1 and user == 2 or computer == 2 and user == 0 ):
        return -1 #When Computer wins the game
    elif(computer == 1 and user == 0 or computer == 2 and user == 1 or computer == 0 and user == 2 ):
        return 1 #When User wins the game
    else:
        print("Wrong input!!\nPlz Enter the correct input") 

#FUNCTION WORK WHEN GAME BETWEEN ONE PLAYER AND SECOND PLAYER
def PointOfPlayerOneandPlayerTwo(playerOne,playerTwo):
    if(playerOne == playerTwo):
        return 0 #When Both Inputs are equal
    elif(playerTwo == 0 and playerOne == 1 or playerTwo == 1 and playerOne == 2 or playerTwo == 2 and playerTwo == 0 ):
        return -1 #When Player Two wins the game
    elif(playerTwo == 1 and playerOne == 0 or playerTwo == 2 and playerOne == 1 or playerTwo == 0 and playerTwo == 2 ):
        return 1 #When Player One wins thw game
    else:
        print("Wrong input!!\nPlz Enter the correct input") 

#WHEN USER CHOSE TWO PLAYER MODE OF GAME
def TwoPlayerGame():
    PlayerOnePoint = 0 #-->POINT OF PLAYER ONE
    PlayerTwoPoint = 0 #--->POINT OF PALYER TWO
    for i in range(0,3):
        #PLAYER ONE INPUTS  
        playerOne = int(input("\nEnter The choice of player One\n0)For Snake\n1)For Water\n2)For Gun\t"))
        #PLAYER TWO INPUTS
        playerTwo = int(input("Enter The choice of player Two\n0)For Snake\n1)For Water\n2)For Gun\t"))
        print("Player One Entered\t",playerOne) #-->PLAYER ONE ENTER YOUR OPTION
        print("Player Two Entered\t",playerTwo) #-->PLAYER TWO ENTER YOUR OPTION
        print("-------------------------------------------------------\n")
        if(PointOfComputerAndPlayer(playerOne, playerTwo) == 1): #CHECK CONDITION AND CALL FUNCTION
            PlayerOnePoint = PlayerOnePoint + 1 #-->Increase the points of Player One
            print("Point For Player One") 
        elif(PointOfComputerAndPlayer(playerOne, playerTwo) == -1):#CHECK CONDITION AND CALL FUNCTION
            PlayerTwoPoint = PlayerTwoPoint + 1 #--> Increase the points of Player Two
            print("Point For Player Two")
        elif(PointOfComputerAndPlayer(playerOne, playerTwo) == 0): #CHECK CONDITION AND CALL FUNCTION
            print("Both Input are Same")               
        print("---------------------------------------------\n")

    print("Player Two Points are\t",PlayerTwoPoint) #-->Total point of Player Two
    print("Player One Points are\t",PlayerOnePoint) #-->Total point of Player One

    if(PlayerOnePoint> PlayerTwoPoint):#Check the Point of Both Players
        print("\n\nGame result is playerOne Win The Game")
    elif(PlayerTwoPoint > PlayerOnePoint):#Check the Point of Both Players
        print("\n\nGame result is playerTwo Win The Game") 
    else:
        print("\n\nGame result is Match Draw") 

    print("------------------------------------------\n")

def PlayWithComputer():
    computerPoint = 0 #-->POINT OF COMPUTER
    userPoint = 0 #-->POINT OF USER
    for i in range(0,3):
        #Computer Inputs
        computer = random.randint(0, 2) #Generates random number using random library
        print("\nEnter ",i + 1,"times " ) #Increase the Value of I
        #User Inputs
        user = int(input("\nEnter The choice For User\n0)For Snake\n1)For Water\n2)For Gun\t"))
        print("User Entered\t\t",user) #-->USER ENTER YOUR OPTION
        print("Computer Entered\t",computer) #-->COMPUTER ENTER YOUR OPTION
        print("-------------------------------------------------------\n")
        if(PointOfComputerAndPlayer(user, computer) == 1):#CHECK CONDITION AND CALL FUNCTION
            userPoint = userPoint + 1 #-->Increase the point of User
            print("Point For User")
        elif(PointOfComputerAndPlayer(user, computer) == -1):#CHECK CONDITION AND CALL FUNCTION
            computerPoint = computerPoint + 1 #-->Increase The Point of Computer
            print("Point For Computer")
        elif(PointOfComputerAndPlayer(user, computer) == 0):#CHECK CONDITION AND CALL FUNCTION
            print("Both Input are Same")               
        print("---------------------------------------------\n")

    print("Computer Points are\t",computerPoint) #-->Total point of Computer
    print("User Points are\t\t",userPoint) #-->Total point of User

    if(userPoint > computerPoint):#Check the Point of Both Players
        print("\n\nGame result is You Win The Game")
    elif(computerPoint > userPoint):
        print("\n\nGame result is You Lose The Game") #Check the Point of Both Players 
    else:
        print("\n\nGame result is Match Draw") 
    print("------------------------------------------\n")
    
#Checking the condition of game mode
if(choice == 1):
    TwoPlayerGame() #Calling function of Two Player Game
elif(choice == 2):
    PlayWithComputer() #Calling function of Computer and User Game
else:
    print("Plz Enter the correct option")    

print("\n--------------------------Thanks for Playing the game--------------------------")
print("-----------------------------------------------------------------------------------")