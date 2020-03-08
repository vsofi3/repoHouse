# GLOBAL VARIABLES
board = ["-","-","-","-","-","-","-","-","-"]
gameStillGoing = True
winner = None
currentPlayer = 'X'

def displayBoard():
    '''
    (NA)-> None

    Displays the game board, using the list "board" in the global space
    '''
    print(board[0] + '|' +board[1] + '|' + board[2])
    print(board[3] + '|' +board[4] + '|' + board[5])
    print(board[6] + '|' +board[7] + '|' + board[8])

def handleTurn(player):
    '''
    (string)-> None

    Handles a single turn of an arbitrary player
    '''
    print(player + "'s turn.")
    position = input('Choose a position from 1 to 9: ')

    valid = False
    while not valid:
    #keeps asking for correct input from user 
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input('Invalid input: Choose a position from 1 to 9:')
        #takes input from user for position- as a string
        position = int(position)-1 #-1 for correct index in the board

        if board[position] == '-':
            valid = True
        else:
            print("You can't go there: try again")
    
    board[position] = player

    displayBoard()

def checkIfGameOver():
    check_for_winner() #criteria for game ending
    check_if_tie()



def check_for_winner():
    global winner #set up global variable

    #check rows,columns, diagonals
    row_winner = checkRows() #returns boolean
    column_winner = checkColumns()
    diagonal_winner = checkDiagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def checkRows():
    global gameStillGoing #set up global variable
    #check if any of the rows have the same value and aren't empty
    row_1 = board[0] == board[1] == board[2] != '-'  #checking first row on board
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        gameStillGoing = False

    if row_1:
        return board[0] #return the winner
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def checkColumns():
    global gameStillGoing #set up global variable
    #check if any of the columns have the same value and aren't empty
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        gameStillGoing = False

    if column_1:
        return board[0] #return the winner
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def checkDiagonals():
    global gameStillGoing #set up global variable
    #check if any of the diagonals have the same value and aren't empty
    diagonal_1 = board[0] == board[4] == board[8] != '-'  #checking first diagonals on board
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    
    if diagonal_1 or diagonal_2:
        gameStillGoing = False

    if diagonal_1:
        return board[0] #return the winner
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global gameStillGoing
    if '-' not in board:
        gameStillGoing = False
    return


def flipP():
    global currentPlayer #global variable 
    if currentPlayer == 'X': #switches players
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    return 
    

def playGame(): #play a game of tic tac toe
    displayBoard() #we want to display the board- first step in game
    while gameStillGoing: 
        handleTurn(currentPlayer) #handle a single turn of a plyer
        checkIfGameOver() #check if the game has ended
        flipP() #flip to the other player

    #the game has ended
    if (winner == 'X') or (winner == 'O'):
        print (winner + ' won.')
    elif winner == None:
        print ('Tie.')
        
        

playGame()
