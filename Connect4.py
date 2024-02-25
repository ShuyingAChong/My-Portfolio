def putChecker(col, playerChecker, board): 
    for row in reversed(range(len(board))):
        if board[row][col] == " ": 
            board[row][col] = playerChecker 
            return True
    return False 

def drawBoard(board):
    for row in range(len(board)):
        print(board[row])

def playerWon(board): 
    playerChecker = "X" 
    for i in range(2): # repeat twice, once for X and once for O 
        
        # checking horizontals
        for row in range(len(board)):
            for col in range(4): # only need to check the first 4 cols for 4-horizontal 
                if lookFor4(row, col, 0, 1, playerChecker, board):
                    return playerChecker
        
        # checking verticals             
        for col in range(len(board[0])):
            for row in range(3): # only need to check the first 3 rows for 4-vertical 
                if lookFor4(row, col, 1, 0, playerChecker, board):
                    return playerChecker 
        
        # checking pos slope diagonals 
        for row in range(3, 6): 
            for col in range(0, 4): 
                if lookFor4(row, col, -1, 1, playerChecker, board):
                    return playerChecker
        
        # checking neg slope diagonals 
        for row in range(0, 3): 
            for col in range(0, 4): 
                if lookFor4(row, col, 1, 1, playerChecker, board):
                    return playerChecker 
        playerChecker = "O" 
    return "None"

def lookFor4(row, col, addR, addC, playerChecker, board): 
    numInARow = 0
    if board[row][col] == playerChecker: 
        numInARow += 1
        i = 1 
        while i < 4:
            if board[row+addR][col+addC] == playerChecker: 
                numInARow += 1
                if addR > 0: 
                    addR += 1
                elif addR < 0:
                    addR -= 1
                if addC > 0:
                    addC += 1
                elif addC < 0:
                    addC -= 1
                i += 1
            else:
                return False
        if numInARow > 3:
            return True
    return False

# create the board and add 6 rows, 7 cols  
board = []
for r in range(6): 
    board.append([]) 
    for c in range(7):
        board[r].append(" ") 

isWon = False 
turnNumber = 1
currentPlayer = "X" 
drawBoard(board)

while (not isWon) and turnNumber < 43: 
    column = int(input(currentPlayer + ", enter the number of the column (1-7) that you would like to place your checker in: "))
    while column > 7 or column < 1 or not putChecker(column - 1, currentPlayer, board): # if it's an invalid column or the column is full 
        column = int(input("Invalid column! " + currentPlayer + ", enter the number of the column (1-7) that you would like to place your checker in: "))
    drawBoard(board)
    turnNumber += 1 

    if playerWon(board) != "None":
        isWon = True
        print("checked playerwon")    
    elif turnNumber % 2 != 0: # it is an odd turn, therefore it is Player1's turn
        currentPlayer = "X"
    elif turnNumber % 2 == 0:
        currentPlayer = "O"

if isWon: 
    print("Congratulations " + playerWon(board) + ", you are the winner!") 
else: # board was filled, game ended in draw 
    print("The game was a draw.") 