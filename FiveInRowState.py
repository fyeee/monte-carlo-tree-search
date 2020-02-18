from State import State
from random import shuffle
import numpy as np


class FiveInRowState(State):
    def __init__(self, board=None, player=1, size=0):
        if board is not None:
            self.size = len(board)
            self.board = board
            self.player = player
        else:
            if size > 0:
                self.board = np.array([np.array([0 for _ in range(size)]) for __ in range(size)])
                self.size = size
                self.player = player
            else:
                raise AttributeError("Size should be greater than 0")

    def pick_random_move(self):
        flatten = list(enumerate(self.board.flatten()))
        shuffle(flatten)
        element = flatten.pop()
        while element[1] != 0:
            element = flatten.pop()
        return element[0] // self.size, element[0] % self.size

    def make_move(self, move):
        new_board = self.board.copy()
        new_board[move[0], move[1]] = self.player
        return FiveInRowState(new_board, -1 * self.player)

    def is_terminal(self):
        # for row in self.board:
        #     count = 0
        #     for cell in row:
        #         if count == 5:
        #             return True
        #         if cell == self.player * -1:
        #             count += 1
        #         else:
        #             count = 0
        for i in range(self.size):
            count_row = 0
            count_column = 0
            for j in range(self.size):
                if count_row == 5 or count_column == 5:
                    return True
                if self.board[i, j] == self.player * -1:
                    count_row += 1
                else:
                    count_row = 0
                if self.board[j, i] == self.player * -1:
                    count_column += 1
                else:
                    count_column = 0

    def __repr__(self):
        if self.player == 1:
            player = 1
        else:
            player = 2
        result = "Current Player is {0}\n".format(player)
        for row in self.board:
            for cell in row:
                if cell == 0:
                    result += ". "
                elif cell == 1:
                    result += "O "
                else:
                    result += "X "
            result += "\n"
        return result


if __name__ == "__main__":
    state = FiveInRowState(size=10)
    new_state = state.make_move((0, 0))
    new_state = new_state.make_move((1, 1))
    new_state = new_state.make_move((0, 1))
    new_state = new_state.make_move((9, 1))
    new_state = new_state.make_move((0, 2))
    new_state = new_state.make_move((7, 2))
    new_state = new_state.make_move((0, 3))
    new_state = new_state.make_move((9, 5))
    new_state = new_state.make_move((0, 4))
    print(new_state.is_terminal())
