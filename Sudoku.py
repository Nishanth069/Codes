import random

M = 9

# Function to print the puzzle
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()

# Function to check if it's safe to place a number in the given cell
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

# Function to solve the Sudoku puzzle using backtracking
def Sudoku(grid, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    for num in range(1, M + 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# Function to generate a random Sudoku puzzle
def generate_sudoku():
    grid = [[0 for _ in range(M)] for _ in range(M)]
    
    # Randomly fill the grid with numbers
    for _ in range(random.randint(30, 50)):  # Number of filled cells
        row, col, num = random.randint(0, M-1), random.randint(0, M-1), random.randint(1, M)
        if grid[row][col] == 0 and solve(grid, row, col, num):
            grid[row][col] = num
    return grid

# Generate a random Sudoku puzzle
grid = generate_sudoku()

print("Generated Sudoku Puzzle:")
puzzle(grid)

if Sudoku(grid, 0, 0):
    print("\nSolved Sudoku Puzzle:")
    puzzle(grid)
else:
    print("Solution does not exist :(")
