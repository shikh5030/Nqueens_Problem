chessboard = [[]]
chessboard = [[0 for i in range(3)] for j in range(3)]   # 0 indicates queen not placed at the (i,j)th position

def check_attack(i, j):
    for k in range(3):
        if chessboard[k][j] == 1:
            return True                # check for queen vertically
    for x in range(3):
        for y in range(3):
            if x+y == i+j or x-y == i-j:
                if chessboard[x][y] == 1:
                    return True
    return False

def Nqueen(row, n):
    if row == n:                     # all queens placed successfully
        return True

    for column in range(n):
        if check_attack(row, column) == False:
            chessboard[row][column] = 1
            if Nqueen(row+1, n) is True:
                return True
            chessboard[row][column] = 0     # backtrack
    return False

Nqueen(0, 3)
for x in range(3):
    for y in range(3):
        print(chessboard[x][y], end='')
    print()