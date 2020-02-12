from State import State
from random import shuffle


class FiveInRowState(State):
    def __init__(self, board, player):
        self.size = len(board)
        self.board = board
        self.player = player

    def pick_random_move(self):
        flatten = list(enumerate(self.board.flatten()))
        shuffle(flatten)
        element = flatten.pop()
        while element[1] == 0:
            element = flatten.pop()
        return element[0] // self.size, element[0] % self.size

    def make_move(self, move):
        new_board = self.board.copy()
        new_board[move[0], move[1]] = self.player
        return new_board

    def is_terminal(self):
        return