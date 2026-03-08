def create_board(n):
    board = []
    for i in range(n):
        board.append(-1)
    return board


def display_board(board, n):
    print("\nFinal Board Configuration:\n")
    
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def check_safe(board, current_row, current_col):
    for previous_row in range(current_row):
        if board[previous_row] == current_col:
            return False

        row_diff = abs(previous_row - current_row)
        col_diff = abs(board[previous_row] - current_col)

        if row_diff == col_diff:
            return False

    return True


def solve_problem(board, current_row, n):
    
    if current_row == n:
        return True

    for col in range(n):

        if check_safe(board, current_row, col):

            board[current_row] = col

            if solve_problem(board, current_row + 1, n):
                return True

           
            board[current_row] = -1

    return False


print("N-Queens Problem Solver")
print("------------------------")

n = int(input("Enter value of N: "))

board = create_board(n)

result = solve_problem(board, 0, n)

if result:
    print("\nSolution Found Successfully!")
    display_board(board, n)
else:
    print("\nNo Solution Exists for this value of N.")