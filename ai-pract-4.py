def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
    # Check the left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    # Check the right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n  # -1 represents an empty row
    backtrack(0)
    return solutions

# Example usage:
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for sol in solutions:
    for i in range(n):
        print(" ".join("Q" if col == sol[i] else "." for col in range(n)))
    print()
