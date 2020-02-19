import math


class Node:
    c = 0.1

    def __init__(self, state, parent=None):
        self.state = state
        self.children = []
        self.parent = parent
        self.visits = 0
        self.reward = 0

    def is_leaf(self):
        return self.state.is_terminal()

    def get_UCT(self):
        return (self.reward / self.visits) + self.c * math.sqrt((math.log(self.parent.visit) / self.visits))

    def add_child(self, state):
        self.children.append(Node(state, self))

    def expand(self):
        move = self.state.pick_random_move()
        self.add_child(self.state.make_move(move))
        return move

    def fully_expanded(self):
        for move in self.state.available_moves():
            if move not in self.children:
                return False
        return True

    def backpropagation(self):
        node = self
        winner = node.state.player * -1
        reward = self.state.get_reward()
        while node:
            node.visits += 1
            if node.state.player == winner:
                node.reward += reward
