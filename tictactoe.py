"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    x = 0
    o = 0

    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1
    if o < x:
        return O
    elif o >= x:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = set()

    for row in range(len(board)):
        for cell in range(len(board[0])):
            if board[row][cell] == EMPTY:
                action.add((row,cell))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    row,cell = action
    new_board = copy.deepcopy(board)
    players = player(board)

    if new_board[row][cell] != EMPTY:
        raise Exception("Your action is not vaild")

    elif new_board[row][cell] == EMPTY:
        new_board[row][cell] = players
        return new_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]

    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]

    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]

    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]

    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]

    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        best_move = None
        v = -math.inf

        for action in actions(board):
            new_board = result(board,action)

            lowest_score = min_value(new_board)

            if lowest_score > v:
                v = lowest_score
                best_move = action

        return best_move
    else:
        v,best_move = math.inf, None

        for action in actions(board):
            new_board = result(board,action)

            highest_score = max_value(new_board)

            if highest_score < v:
                v = highest_score
                best_move = action

        return best_move

def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):

        v = min(v, max_value(result(board,action)))
    return v






