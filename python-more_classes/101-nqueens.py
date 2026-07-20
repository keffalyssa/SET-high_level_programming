#!/usr/bin/python3
"""Solves the N queens puzzle."""
import sys


def solve_nqueens():
    """Main function to handle argument validation and solve N queens."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        """Check if it's safe to place a queen at row, col."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        """Recursive backtracking function to find all solutions."""
        if row == n:
            solutions.append([[r, board[r]] for r in range(n)])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    solve_nqueens()
