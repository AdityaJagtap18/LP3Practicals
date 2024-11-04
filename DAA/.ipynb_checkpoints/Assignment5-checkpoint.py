# Python3 program to solve N Queen Problem using backtracking

global N
N = 4

# Function to print the solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()  # To separate the solution visually

# A utility function to check if a queen can be placed on board[row][col]
# We only need to check the left side for attacking queens
def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# A recursive utility function to solve the N-Queen problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing the queen in board[i][col] doesn't lead to a solution,
            # remove the queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

# This function solves the N-Queen problem using backtracking.
# It prints one feasible solution.
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver code to test the solution
solveNQ()


"""
PS E:\JAVA> & C:/Users/tejas/AppData/Local/Microsoft/WindowsApps/python3.11.exe e:/JAVA/Assignment5.py
0 0 1 0 
1 0 0 0 
0 0 0 1 
0 1 0 0 


"""