"""
Tic Tac Toe Player
"""

import math
import copy

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
        return 'X'

    # It's no one's turn if it's a terminal board
    elif terminal(board) == True:
        return None
    x_count = 0
    o_count = 0
    
    """
    Since X always has the 1st move, the move count of both players is equal
    when it's X's turn, and X's move count is bigger when it's O's turn
    """

    else:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 'X':
                    x_count += 1
                elif board[i][j] == 'O':
                    o_count += 1
        if x_count > o_count:
            return 'O'
        elif x_count == o_count:
            return 'X'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 'EMPTY':
                action_tuple = (i, j)
                possible_moves.append(action_tuple)
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

    original_board_copy = copy.deepcopy(board)
    new_board = board
    new_board[i][j] = move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == 'X' or \
                board[i][j] == board[i + 1][j] == board[i + 2][j] == 'X' or \
                board[0][0] == board[1][1] == board[2][2] == 'X' or \
                board[2][0] == board[1][1] == board[0][2] == 'X':
                    return 'X'
            
            elif board[i][j] == board[i][j + 1] == board[i][j + 2] == 'O' or \
                board[i][j] == board[i + 1][j] == board[i + 2][j] == 'O' or \
                board[0][0] == board[1][1] == board[2][2] == 'O' or \
                board[2][0] == board[1][1] == board[0][2] == 'O':
                    return 'O'
            
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
            if board[i][j] == 'EMPTY':
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

    if if_terminal == True:
        if game_winner == 'X':
            return 1
        elif game_winner == 'O':
            return -1
        elif game_winner == None:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == 'O':
        best_move = None
        actions_set = actions(board)
        if terminal(board) is True:
            return None
        else:
            for action in actions_set:
                move = result(board, action)
                if utility(move) <= utility(board):
                    opponent_action = minimax(move)
                    if utility(opponent_action) != 1:
                        best_move = move
                        minimax(best_move)
            return best_move
            
    
    if player(board) == 'X':
        best_move = None
        actions_set = actions(board)
        if terminal(board) is True:
            return None
        else:
            for action in actions_set:
                move = result(board, action)
                if utility(move) >= utility(board):
                    opponent_action = minimax(move)
                    if utility(opponent_action) != -1:
                        best_move = move
                        minimax(best_move)
            return best_move
