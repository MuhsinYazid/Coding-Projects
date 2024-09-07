#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

#Update the gameboard with the user input
def markBoard(position, mark):
    board[position]=mark
    


#Print the game board as described at the top of this code skeleton
def printBoard():
    print('Box No. Guide: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')
    print(" ")
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print(" --------- ")
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print(" --------- ")
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9] )
    return


#Validate move by players
def validateMove(position):
    if isinstance(position, str) and position.isdigit():
        position = int(position)

    if isinstance(position, int) and 1 <= position <= 9 and board[position] == ' ':
        return True
    return False

#List of winning combination on board
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

#Check if any of the p[layers won the game
def checkWin(player):
    for win in winCombinations:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False


#Check if the game is tie
def checkFull():
    for value in board:
        if board[value] == ' ':
            return False
    return True

#GAME LOGIC
def game_start():# entry point of the whole program
    global gameEnded, currentTurnPlayer
    gameEnded = False
    currentTurnPlayer = 'X'
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
    print(" ")
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print(" --------- ")
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print(" --------- ")
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9] )

    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ") #Input position of players role
        if validateMove(move):
            markBoard(int(move), currentTurnPlayer)

            if checkWin(currentTurnPlayer):
                printBoard()
                print("Player {} wins!".format(currentTurnPlayer))
                gameEnded = True
                break

            if checkFull():
                printBoard()
                print("Tie game!")
                gameEnded = True
                break

            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
        else:
            print("Invalid move")
        
        printBoard()

#Restart the match
def empty_board():#Clean the board with any value
    global board 
    board = {}  
    for value in range(1, 10):
        board[value] = ' '  

def game_loop():#Loop the game if players wanted to restart
    while True:
        game_start()
        restart = input("Do you want to play again? (Y:yes/N:no): ").lower()
        if restart not in ['y', 'yes']:
            print("GAME OVER")
            break
        else:
            empty_board()
            print('New Game')

#Start the game
game_loop()
