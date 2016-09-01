"""
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0]
and destination block is lower rightmost block i.e., maze[N-1][N-1].
A rat starts from source and has to reach destination. The rat can move in only 2 directions, either bottom or right.
In the maze matrix, 0 means the block is dead end and 1 means the block can be used in the path from source to destination.
"""
def findPath(maze):
    n = len(maze)
    sol = [[0 for i in range(n)] for j in range(n)]
    if bactrack(maze, n, sol, 0, 0) == False:
        return False
    else:
        return sol

def bactrack(maze, n, sol, row, col):
    if row == n-1 and col == n-1:
        sol[row][col] = 1
        return True
    if isSafe(row, col, n):
        sol[row][col] = 1
        if bactrack(maze, n, sol, row+1, col): return True # Bottom
        if bactrack(maze, n, sol, row, col+1): return True # Right

        sol[row][col] = 0

    return False

def isSafe(row, col, n):
    if (row >=0) and (row < n) and (col >=0) and (col < n) and maze[row][col] == 1:
        return True
    return False

# Test
maze = [[1,0,0,0],[1,0,0,1],[0,1,0,0],[1,1,1,1]]
path = findPath(maze)
if path:
    print path
else:
    print "No such path"