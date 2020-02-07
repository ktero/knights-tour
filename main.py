"""
Solving the knight's tour problem using the Warnsdorff's algorithm.
"""

import os
from colorama import init, Fore
from time import sleep
from inputs import print_empty_board, clear, validate_input
from heapq import heappush, heappop

# Board size N x N
N = 8
T = N * N

# Knight's x and y movement
MX = [1, 2, 2, 1, -1, -2, -2, -1]
MY = [-2, -1, 1, 2, 2, 1, -1, -2] 


def print_board(board):
    """
    Print the NxN chess board.
    """
    print()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print(Fore.YELLOW + '{:4d}'.format(board[i][j]), end=' ')
            elif board[i][j] == T:
                print(Fore.GREEN + '{:4d}'.format(board[i][j]), end=' ')
            else:
                print('{:4d}'.format(board[i][j]), end=' ')
        print()


def get_progress(board):
    """
    Returns the progress of the algorithm
    """
    visited_cell = 0
    total_cell = T

    for row in range(N):
        visited_cell += (N - board[row].count(0))

    progress = (visited_cell / total_cell) * 100

    return f'{ progress }%'


def is_safe(x, y, board):
    """
    Check if the position did not exceed the borders and if the cell is empty.
    """
    if 0 <= x < N and 0 <= y < N and board[x][y] == 0:
        return True
    return False


def get_degree(x, y, board):
    """
    Returns the number of empty squares adjacent to (x, y)
    """
    c = 0
    for i in range(N):
        if is_safe(x + MX[i], y + MY[i], board):
            c += 1
    return c


def algorithm(x, y, board):
    """
    Warnsdorff's algorithm:
        1. Set P to be a random initial position on the board.
        2. Mark the board at P with the move number "1".
        3. Do following for each move number from 2 to the number of squares on the board.
            - Let S be the set of positions accessible from P.
            - Set P to be the position in S with minimum accessibiltiy.
            - Mark the board at P with the current move number.
        4. Return the marked board - each square will be marked with the move number on which it is visited.
    """
    # Set starting position of the knight
    p = 1
    board[x][y] = p
    
    for _ in range(T):
        pq = []

        for i in range(8):
            nx = x + MX[i]
            ny = y + MY[i]
            
            if is_safe(nx, ny, board):
                # Get the index of the position with minimum accessibility.
                c = get_degree(nx, ny, board)
                heappush(pq, (c, i))
        
        if len(pq) > 0:
            (_, m) = heappop(pq)
            x += MX[m]
            y += MY[m]
            p += 1
            board[x][y] = p

            # Print board and progress bar 
            print("Completed: {}".format(get_progress(board)))
            print_board(board)

            if not p == T:
                sleep(0.5)
                clear()
            else:
                input("\nPress Enter to continue...")


if __name__ == "__main__":

    while True:
        clear()

        print_empty_board()

        # Input starting position of the knight.
        p = input("Knight\'s starting position (row, column): ")

        if validate_input(p):
            break
        else:
            print('Invalid, Try again')
            sleep(1)

    clear()
    
    # Initialize board with no marks.
    x, y = list(map(int, p.split(',')))
    b = [[0 for i in range(N)] for i in range(N)]
    
    init(autoreset=True) # Colorama
    algorithm(x, y, b)