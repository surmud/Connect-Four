# File:    design1.txt
# Author:  Surmud Jamil
# Date:    Oct 28, 2018
# Section: 7
# E-mail:  sjamil2@umbc.edu
# Description: This program allows you to play connect four



from random import randint, seed 
seed(100)                        


PLAYER_1_PIECE = "x"
PLAYER_2_PIECE = "o"
MIN_BOARD_LENGTH = 5
WIN_DISTANCE = 3

# checkValidMove() checks if a move is valid or not
#input: The gameboard and the position where the piece is being dropped 
#output: A true or false value of whether the move is valid or not
def checkValidMove(gameBoard, dropPosition):
    validMove = True
    bottomRow = len(gameBoard) - 1
    if dropPosition <= 0 or dropPosition > len(gameBoard):
        validMove = False

    else:
        while bottomRow >= 0 and \
        (gameBoard[bottomRow][dropPosition - 1] == PLAYER_2_PIECE or \
        gameBoard[bottomRow][dropPosition - 1]== PLAYER_1_PIECE):
            bottomRow = bottomRow - 1
        if bottomRow < 0:
            validMove = False
 
    return validMove

#checkWin() checks if a person has won the game or not
#input: the gameBoard with all the pieces on it, the person who's turn 
#.      it is, and the column and row of where the piece is being drop
#output: returns a true or false value if a win exists or not
def checkWin(gameBoard, playerTurn, column, row):
    column = column - 1
    boardLength = len(gameBoard) - 1
    boardHeight = len(gameBoard[1])  
    winOrNah = False
    #locationOfPiece = gameBoard[row][column]
    


    if (row < (boardHeight - WIN_DISTANCE)):
        #check the down direction for a win 
        if gameBoard[row][column] == gameBoard[row + 1][column] and \
            gameBoard[row][column] == gameBoard[row + 2][column] and \
                gameBoard[row][column] == gameBoard [row + 3][column]:

            winOrNah = True
            

    if column <= boardLength - WIN_DISTANCE:
        #check the right direction for a win
        if gameBoard[row][column] == gameBoard[row][column + 1] and \
            gameBoard[row][column] == gameBoard[row][column + 2] and \
            gameBoard[row][column] == gameBoard [row][column + 3]:

            winOrNah = True

    if column >= WIN_DISTANCE:
        #check the left direction for a win
        if gameBoard[row][column] == gameBoard[row][column - 1] and \
            gameBoard[row][column] == gameBoard[row][column - 2] and \
            gameBoard[row][column] == gameBoard [row][column - 3]:

            winOrNah = True

    if ((column >= (boardLength - WIN_DISTANCE)) and \
        (row >= (boardHeight - WIN_DISTANCE))):
        #check the left-up diagonal direction for a win
        if gameBoard[row][column] == gameBoard[row - 1][column - 1] and \
            gameBoard[row][column] == gameBoard[row - 2][column - 2] and \
            gameBoard[row][column] == gameBoard[row - 3][column - 3]:

            winOrNah = True

    if row >= boardHeight - WIN_DISTANCE and \
        column <= boardLength - WIN_DISTANCE:
        #check the right-up diagonal for a win
        if gameBoard[row][column] == gameBoard[row - 1][column + 1] and \
            gameBoard[row][column] == gameBoard[row - 2][column + 2] and \
            gameBoard[row][column] == gameBoard[row - 3][column + 3]:

            winOrNah = True


    if row < boardHeight - WIN_DISTANCE and \
        column > boardLength - WIN_DISTANCE:
        #check the down-left diagonal for a win
        if gameBoard[row][column] == gameBoard[row + 1][column - 1] and \
            gameBoard[row][column] == gameBoard[row + 2][column - 2] and \
            gameBoard[row][column] == gameBoard[row + 3][column - 3]:

            winOrNah = True

    if column <= boardLength - WIN_DISTANCE and \
        row <= boardHeight - WIN_DISTANCE:
        #check the down-right diagonal for a win
        if  gameBoard[row][column] == gameBoard[row + 1][column + 1] and \
            gameBoard[row][column] == gameBoard[row + 2][column + 2] and \
            gameBoard[row][column] == gameBoard[row + 3][column + 3]:

            winOrNah = True 

    if column >= 1:
        #check 1 space to the left of index and 2 to the right for a win
        if gameBoard[row][column] == gameBoard[row][column - 1] and \
            gameBoard[row][column] == gameBoard[row][column + 1] and \
            gameBoard[row][column] == gameBoard[row][column + 2]:

            winOrNah = True

    if column >= 2:
        #check 1 space to the right and 2 spaces to the left of index for a win
        if gameBoard[row][column] == gameBoard[row][column - 1] and \
            gameBoard[row][column] == gameBoard[row][column - 2] and \
            gameBoard[row][column] == gameBoard[row][column + 1]:

            winOrNah = True

    
        #check +1 up-right and -2 diagonal left of index for a win
        #if gameBoard[row][column] == gameBoard[row + 1][column + 1] and \
            #gameBoard[row][column] == gameBoard[row - 1][column - 1] and \
            #gameBoard[row][column] == gameBoard[row - 2][column  - 2]:

    return winOrNah


#       drops the piece and updates the gameboard after the piece is dropped
#input: the person dropping the piece the game board and the column where the 
#       person wants to drop it
#output: returns the y coordinate of the piece being dropped so it 
#        can be used later
def dropPeice(playerNum, gameBoard, location):
    location = location - 1
    bottomRow = len(gameBoard) - 1
    if playerNum == "Player 1":
        pieceDropped = PLAYER_1_PIECE

    elif playerNum =="Player 2" or playerNum == "Computer":
        pieceDropped = PLAYER_2_PIECE

    while gameBoard[bottomRow][location] == PLAYER_2_PIECE \
        or gameBoard[bottomRow][location]== PLAYER_1_PIECE:
        bottomRow = bottomRow - 1
    #loop so that if a row already has a piece on it, it drops\
    #on the row above
    gameBoard[bottomRow][location] = pieceDropped

    return bottomRow
    
#printBoard() displays the current game board with the numbers lined across
#input: the list "gameboard" and the list of nums
#ouput: none
def printBoard(gameBoard, gameBoardNums):
    indexNums = 0
    print("Column Number:\n")
    while indexNums < len(gameBoardNums):
        print(gameBoardNums[indexNums], end = " ")
        indexNums = indexNums + 1
    print()

    for index in range(0, len(gameBoard)):
        for index2 in range(0, len(gameBoard[index]) ):
            print(gameBoard[index][index2], end=" ")
        print()   
        

def main():
    clearScreen = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(clearScreen)
    invalidOptionText = "Invalid input, please enter again"
    playOrNah = input("Do you want to play connect four? (y/n): ")
    gameBoard = []
    gameBoardNums = []
    num = 1
    if playOrNah == "n":
        print(clearScreen)
        print("I too wouldn't play if I sucked as bad as you\n\n")
        
    while playOrNah != "y" and playOrNah != "n":
        print(invalidOptionText)
        playOrNah = input("Do you want to play connect four? (y/n): ")

    while playOrNah == "y":
        gameBoard = []
        numMovesMade = 0

        boardHeight = int(input("How many rows tall do you want the game "\
            "board to be?: "))
        while boardHeight < MIN_BOARD_LENGTH:
            print("The board must be at least 5 slots tall, please enter again.")
            boardHeight = int(input("How many rows tall do you want the game "\
            "board to be?: "))

        boardLength = int(input("How many columns wide do you want the game"\
            " board to be?: "))
        while boardLength < MIN_BOARD_LENGTH:
            print("The board must be at least 5 slots wide, please enter again.")
            boardLength = int(input("How many columns wide do you want the game"\
            " board to be?: "))



        while len(gameBoardNums) < boardLength:
            gameBoardNums.append(num)
            num = num + 1
           

        while len(gameBoard) < boardHeight:
            boardRow = []
            while len(boardRow) < boardLength:
                boardRow.append("_")
            gameBoard.append(boardRow)

        playComputer = input("Do you want to play against the computer? "\
                             "(y/n): ")
        if playComputer == "y":
            player2 = "Computer"    
        elif playComputer == "n":
            player2 = "Player 2"

        while playComputer != "y" and playComputer != "n":
            print(invalidOptionText)
            playComputer = input("Do you want to play against the"\
                                " computer? (y/n): ")
        turnValue = 0
        gameOver = False
        while gameOver == False:
            print(clearScreen)
            printBoard(gameBoard, gameBoardNums)
            player1Turn = True

            if turnValue % 2 == 0:
                playerTurn = "Player 1"

            if turnValue % 2 == 1:
                playerTurn = player2

            if playerTurn =="Player 1" or player2 == "Player 2":
                dropChoice = int(input(playerTurn+" it's your turn, which"\
                            " column do you want to drop your peice?: "))

            if playerTurn == player2 and player2 == "Computer":
                dropChoice = randint(1, boardLength)
                #Make sure that the computer hits a valid spot 
                while checkValidMove(gameBoard, dropChoice) == False:
                    dropChoice = randint(1, boardLength)
                
            while checkValidMove(gameBoard, dropChoice) == False:
                print("Invalid Move, please enter again")
                dropChoice =int(input(playerTurn+" it's your turn, which"\
                            " column do you want to drop your peice?: "))
                
            #checks if the move they wanna make is valid, if it's valid, drop
            # the piece.
            
            if checkValidMove(gameBoard, dropChoice) == True:    
                rowValue = dropPeice(playerTurn, gameBoard, dropChoice)
                printBoard(gameBoard, gameBoardNums)

                if checkWin(gameBoard, playerTurn, dropChoice, rowValue) == True:
                    # printBoard(gameBoard, gameBoardNums)
                    print(playerTurn, "has won the game!")
                    gameOver = True

            #if the number of moves made is bigger than the board length, 
            #the game becomes a draw 

            numPossibleMoves = (boardLength * boardHeight) - 1
            if numMovesMade >= numPossibleMoves:
                print("The game is a draw")
                gameOver = True

            turnValue = turnValue + 1
            numMovesMade = numMovesMade + 1
            

        playOrNah = input("Do you want to play again? (y/n): ")
        if playOrNah == "n":
            print(clearScreen)
            print("I too wouldn't play if I sucked as bad as you\n\n")

        while playOrNah != "y" and playOrNah != "n":
            print(invalidOptionText)
            playOrNah = input("Do you want to play connect four? (y/n): ")
main()























