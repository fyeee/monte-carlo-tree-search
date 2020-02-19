from State import State
import random
import numpy as np


class FiveInRowState(State):
    def __init__(self, board=None, player=1, size=0):
        super().__init__()
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

    def available_moves(self):
        result = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == 0:
                    result.append((i, j))
        return result

    def pick_random_move(self):
        all_moves = self.available_moves()
        return random.choice(all_moves)

    def make_move(self, move):
        new_board = self.board.copy()
        new_board[move[0], move[1]] = self.player
        return FiveInRowState(new_board, -1 * self.player)

    def is_terminal(self):
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

        for i in range(4, self.size):
            for j in range(self.size - 4):
                if self.board[i, j] == self.player * -1 and self.board[i - 1, j + 1] == self.player * -1 and \
                        self.board[i - 2, j + 2] == self.player * -1 and self.board[i - 3, j + 3] == self.player * -1 \
                        and self.board[i - 4, j + 4] == self.player * -1:
                    return True

        for i in range(4, self.size):
            for j in range(4, self.size):
                if self.board[i, j] == self.player * -1 and self.board[i - 1, j - 1] == self.player * -1 and \
                        self.board[i - 2, j - 2] == self.player * -1 and self.board[i - 3, j - 3] == self.player * -1 \
                        and self.board[i - 4, j - 4] == self.player * -1:
                    return True
        return False

    def get_reward(self):
        return 1

    def __repr__(self):
        if self.player == 1:
            player = 1
        else:
            player = 2
        result = "Current Player: Player {0}\n".format(player)
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
    new_state = state.make_move((4, 0))
    new_state = new_state.make_move((1, 2))
    new_state = new_state.make_move((3, 1))
    new_state = new_state.make_move((9, 1))
    new_state = new_state.make_move((2, 2))
    new_state = new_state.make_move((7, 2))
    new_state = new_state.make_move((1, 3))
    new_state = new_state.make_move((9, 5))
    print(new_state.is_terminal())
    new_state = new_state.make_move((0, 4))
    print(new_state)
    print(new_state.is_terminal())
