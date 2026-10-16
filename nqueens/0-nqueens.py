#!/usr/bin/python3
"""Solves the N queens puzzle."""

import sys


def solve_nqueens(n):
    """Solve N-queens puzzle and print every possible solution."""

    def backtrack(row, queens, cols, diag1, diag2):
        if row == n:
            print(queens)
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            queens.append([row, col])
            backtrack(row + 1, queens, cols, diag1, diag2)
            queens.pop()
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

    backtrack(0, [], set(), set(), set())


def main():
    """Validate arguments and run N-queens solver."""
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
