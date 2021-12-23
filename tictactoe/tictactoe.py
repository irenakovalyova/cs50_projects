"""
Tic Tac Toe Player
"""

import math
import copy
from types import NoneType

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
    # X player always goes first
    if board == initial_state():
        return X

    # It's no one's turn if it's a terminal board
    elif terminal(board) == True:
        return None
    x_count = 0
    o_count = 0
    
    """
    Since X always has the 1st move, the move count of both players is equal
    when it's X's turn, and X's move count is bigger when it's O's turn
    """

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    if x_count > o_count:
        return O
    elif x_count == o_count:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                action_tuple = (i, j)
                possible_moves.add(action_tuple)
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actions_set = set()
    actions_set = actions(board)
    if action not in actions_set:
        raise NameError('Not a valid move')
    move = player(board)
    i = action[0]
    j = action[1]

    new_board = copy.deepcopy(board)
    new_board[i][j] = move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Vertical win
    for i in range(0, 3):
        if (board[0][i] != None and board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            return board[0][i]
                
    # Horizontal win
    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'

    # Diagonal win from left to right
    if (board[0][i] != None and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[0][0]

    # Diagonal win from right to left
    if (board[0][2] != None and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[0][2]
           
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_winner = winner(board)
    if game_winner is not None:
        return True

    empty_count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                empty_count +=1

    if empty_count == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    game_winner = winner(board)
    if_terminal = terminal(board)

    score = 0
    if if_terminal == True:
        if game_winner == X:
            score = 1
        elif game_winner == O:
            score = -1
        elif game_winner == None:
            score = 0
    return score


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentactions = actions(board)
    if player(board) == X:
        max_value = -2
        move = set()
        for action in currentactions:
            current_value = maximum(result(board, action))
            if current_value > max_value:
                max_value = current_value
                move = action
    else:
        min_value = 2
        move = set()
        for action in currentactions:
            current_value = minimum(result(board, action))
            if current_value < min_value:
                min_value = current_value
                move = action
    return move

def maximum(board):
    """
    Returns maximum value of the current board by calculating future moves
    """

    if terminal(board) is True:
        return utility(board)

    max_value = -2
    actions_set = actions(board)

    for action in actions_set:
        value_result_board = minimum(result(board, action))
        max_value = max(max_value, value_result_board)
    
    return max_value

def minimum(board):
    """
    Returns minimum value of the current board by calculating future moves
    """

    if terminal(board) is True:
        return utility(board)

    min_value = 2
    actions_set = actions(board)

    for action in actions_set:
        value_result_board = maximum(result(board, action))
        min_value = min(min_value, value_result_board)
    
    return min_value
