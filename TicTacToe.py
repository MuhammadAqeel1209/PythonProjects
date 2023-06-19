def BoardPrint(xState,yState):
    zero  = 'X' if xState[0] else ('O' if yState[0] else 0)
    one   = 'X' if xState[1] else ('O' if yState[1] else 1)
    two   = 'X' if xState[2] else ('O' if yState[2] else 2)
    three = 'X' if xState[3] else ('O' if yState[3] else 3)
    four  = 'X' if xState[4] else ('O' if yState[4] else 4)
    five  = 'X' if xState[5] else ('O' if yState[5] else 5)
    six   = 'X' if xState[6] else ('O' if yState[6] else 6)
    seven = 'X' if xState[7] else ('O' if yState[7] else 7)
    eight = 'X' if xState[8] else ('O' if yState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--| --|--")
    print(f"{three} | {four} | {five}")
    print("--| --|--")
    print(f"{six} | {seven} | {eight}")
    print("--| --|--")

def Sum(a,b,c):
    return a + b + c

def CheckWin(xState,yState):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #-->Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #-->Columns
        [0, 4, 8], [2, 4, 6]  #-->Diagonals
    ]

    for combine in winning_combinations:
        if Sum(xState[combine[0]],xState[combine[1]],xState[combine[2]])== 3:
            print("\nX win the game\n")
            return 0
        if Sum(yState[combine[0]],yState[combine[1]],yState[combine[2]]) == 3:
            print("\nO win the game\n")
            return 1 
    return -1;    



print("-----------------------------------------------------------------------")
print("----------------------------Welcome In---------------------------------")
print("--------------------------- Tic Tac Toe -------------------------------")
print("--------------------------- Game(T T T) -------------------------------")
print("-----------------------------------------------------------------------")
xState = [0,0,0,0,0,0,0,0,0]
yState = [0,0,0,0,0,0,0,0,0]
turn = 1
chance = 0
while(True):
    BoardPrint(xState,yState)
    if(turn == 1):
        print("\nX,s Chance")
        value = int(input("\nEnter the value "))
        xState[value] = 1
    else:
        print("\n0,s Chance")
        value = int(input("\nEnter the value "))
        yState[value] = 1 
    chance = chance + 1
    win = CheckWin(xState, yState)  
    if win != -1:
        break
    if(chance == 9):
        print("\n\nGame is tie\n")
        break
    turn = 1 - turn
BoardPrint(xState, yState)
print("Thanks For Playing ")    
