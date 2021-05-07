def is_solved(board):
    a = set([board[0][0], board[1][1],board[2][2]])
    b = set([board[0][2], board[1][1],board[2][0]])
    if (len(a) == 1 and board[1][1] != 0):
            return board[1][1]
    elif (len(b) == 1 and board[1][1] != 0):
        return board[1][1]
    
    for x in range(3):
        a = set([board[x][0], board[x][1], board[x][2]])
        b = set([board[0][x], board[1][x], board[2][x]])
        if (len(a) == 1 and board[x][x] != 0):
            return board[x][x]
        elif (len(b) == 1 and board[x][x] != 0):
            return board[x][x]
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 0):
                return -1
    
    return 0

board = [[2, 2, 2],
         [0, 1, 1],
         [1, 0, 0]]
print(is_solved(board)) # winner 2

board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
print(is_solved(board)) # winning row 1

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board)) # winning column 1

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
print(is_solved(board)) # it must be equal it means 0