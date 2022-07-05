# Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, 
# we've decided to simplify the game. Here are our assumptions:
# The computer (i.e., your program) should play the game using 'X's;
# The user (e.g., you) should play the game using 'O's;
# The first move belongs to the computer - it always puts its first 'X' in the middle of the board;
# All the squares are numbered row by row starting with 1 (see the example session below for reference)
# The user inputs their move by entering the number of the square they choose - the number must be valid, 
# i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# The program checks if the game is over - there are four possible verdicts: the game should continue, 
# or the game ends with a tie, your win, or the computer's win;
# The computer responds with its move and the check is repeated;
# Don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.

"""
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8

"""

from random import randrange

board = [[1,2,3], [4,5,6], [7,8,9]]

def DisplayBoard(board):
    """
    It receives as parameter the board and prints it.

    Args:
        board (list): current state of the board.
    """
    print("+-------" * 3,"+", sep="") # +-------+-------+-------+
    for row in range(3):
        print("|       " * 3,"|", sep="") # |       |       |       | * 3
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="") # |   1   |   2   |   3    to 7, 8 and 9
        print("|") # The missin one from the previous iteration
        print("|       " * 3,"|",sep="") # Another row
        print("+-------" * 3,"+",sep="")

def EnterMove(board):
    """
    It receives the current board, asks the user to enter a move and 
    updates the board according to the user's decision.

    Args:
        board (list): current state of the board.
    """
    try:
        move = int(input("Enter your move:"))
        assert move > 0 and move < 10 # Validates move.
        
        for row in range(3):
            for col in range(3):
                if move == board[row][col]:
                    board[row][col] = "O" # Update element.
    except AssertionError:
        print("Enter a correct value from 1 to 9.")
    except ValueError:
        print("Enter an integer.")

def MakeListOfFreeFields(board):
    """
    It examines the board and makes a list of free fields.
    The list is made of tuples, each tuple contains each row and column.

    Args:
        board (list): current state of the board.
    
    Returns:
        free_fields (list): list of free fields.
    """
    free_fields = []
    for row in range(3):
            for col in range(3):
                if (not board[row][col] == 'O') and (not board[row][col] == 'X'):
                    free_fields.append((row, col))
    return free_fields     

DisplayBoard(board)
EnterMove(board)
DisplayBoard(board)
print(MakeListOfFreeFields(board))


def VictoryFor(board, sign):
    """
    It analyses the state of the board to check whether the user or
    the machne has won.

    Args:
        board (list): current state of the board.
        sign (string): O or X.
    """
    

# def DrawMove(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.

# for i in range(10):
#     print(randrange(8))