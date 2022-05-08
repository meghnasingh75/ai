# ALGORITHM:
# 1. Start in the leftmost column. 
# 2. If all queens are placed return true 
# 3. Try all rows in the current column. Do the following for every tried row. 
#     a. If the queen can be placed safely in this row then mark this [row, column] 
#         as part of the solution and recursively check if placing queen here leads to 
#         a solution. 
#     b. If placing queen in [row, column] leads to a solution then return true. 
#     c. If placing queen doesn't lead to a solution then unmark this [row, column] 
#         (Backtrack) and go to step (a) to try other rows. 
# 4. If all rows have been tried and nothing worked, return false to trigger 
#     backtracking. 
# 5. End. 



N=int(input("enter no of queens : ")) 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ") 
        print(" ")

def isSafe(board,row,col): 
    for i in range(col):
        if board[row][i]=='Q': 
            return False

    for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
        if board[i][j]=='Q':
            return False

    for i,j in zip(range(row,N,1), range(col,-1,-1)): 
        if board[i][j]=='Q':
            return False 
    return True

def solveNQUtil(board,col): 
    if col>=N:
        return True

    for i in range(N):
        if isSafe(board,i,col): 
            board[i][col]='Q'
            if solveNQUtil(board,col+1) == True: 
                return True
            board[i][col]=0 
    return False

def solveNQ():
    board = [[0 for i in range(N)] for j in range(N)]

    if solveNQUtil(board,0)==False: 
        print("Solution does not exist") 
        return False
    printSolution(board) 
    return True

solveNQ()