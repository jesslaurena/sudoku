import math,random

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length


    '''


    def __init__(self, removed_cells=0, row_length=9):

        choice = input("Choose difficulty level (easy, medium, hard): ").lower()
        if choice == "easy":
            removed_cells = 30
        elif choice == "medium":
            removed_cells = 40
        elif choice == "hard":
            removed_cells = 50
        else:
            print("Invalid choice. Defaulting to easy.")
            removed_cells = 30

        self.row_length = row_length
        self.box_length = int(row_length ** 1/2)
        self.removed_cells = removed_cells
        self.board = self.initialize()

    def initialize(self):
        return [["-" for _ in range(self.row_length)] for _ in range(self.row_length)]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        pass

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''


    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for i in range(self.row_length):
            if self.board[row][i] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][int(col)] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        row_start = (row_start // 3)
        col_start = (col_start // 3)
        for i in range(row_start * 3, row_start *3 + 3):
            for j in range(col_start * 3, col_start*3 + 3):
                if self.board[i][j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        return False


    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        num_list = []
        for row in range(3):
            for col in range(3):
                x = random.randint(1, 9)
                while x in num_list:
                    x = random.randint(1, 9)
                self.board[row_start + row][col_start + col] = x
                num_list.append(x)

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    # def fill_remaining(self, row, col):
    #     if (col >= self.row_length and row < self.row_length - 1):
    #         row += 1
    #         col = 0
    #     if row >= self.row_length and col >= self.row_length:
    #         return True #full board
    #     if row < self.box_length:
    #         if col < self.box_length:
    #             col = self.box_length
    #     elif row < self.row_length - self.box_length:
    #         if col == int(row // self.box_length * self.box_length):
    #             col += self.box_length
    #     else:
    #         if col == self.row_length - self.box_length:
    #             row += 1
    #             col = 0
    #             if row >= self.row_length:
    #                 return True
    #
    #     for num in range(1, self.row_length + 1):
    #         if self.is_valid(row, col, num):
    #             self.board[row][col] = num
    #             if self.fill_remaining(row, col + 1):
    #                 return True
    #         self.board[row][col] = 0
    #     return False

    def fill_remaining(self, row, col):
        if row == self.row_length - 1 and col == self.row_length:  # Base case: end of board
            return True
        if col == self.row_length:  # Move to next row
            row += 1
            col = 0

        # Skip pre-filled diagonal cells
        if self.board[row][col] != "-":
            return self.fill_remaining(row, col + 1)

        # Try placing digits
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = "-"  # Backtrack

        return False  # Trigger backtracking

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 0)



    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

board = SudokuGenerator(0,9)
board.fill_values()
board.print_board()