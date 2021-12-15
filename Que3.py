def getBoard():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    for row in range(3):
        for col in range(3):
            board[row][col] = int(input(f'Please enter the value of row {row+1}, column {col+1} (1 for X, 2 for O and 0 for none) : '))
    return(board)

def detectWinnerByLoops(board):
    winner = 0
    for num in range(3): # Check rows & columns
        if board[num][0] == board[num][1] and board[num][1] == board[num][2] and board[num][0] != 0:
            winner = board[num][0]
        elif board[0][num] == board[1][num] and board[1][num] == board[2][num] and board[0][num] != 0:
            winner = board[0][num]
     # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        winner = board[1][1]
    if winner != 0:
        print(f'According to detectWinnerByLoops the winner is {winner}.')
    else:
        print(f'According to detectWinnerByLoops in this game there is no winner.')

def detectWinnerBySets(board):
    cols = [[lst[indx] for lst in board] for indx in range(3)]
    diagnol1 = list([board[indx][indx] for indx in range(3)])
    diagnol2 = [board[0][2], board[1][1], board[2][0]]
    for lst in cols: 
        board.append(lst)
    board.append(diagnol1)
    board.append(diagnol2)
    for lst in board:
        if len(set(lst)) == 1 and list(set(lst)) != [0]:
            winner = list(set(lst))
            print(f'According to detectWinnerBySets the winner is {winner[0]}.')
            break
    else:
        print(f'According to detectWinnerBySets in this game there is no winner.')

# main script

board = getBoard()
detectWinnerByLoops(board)
detectWinnerBySets(board)