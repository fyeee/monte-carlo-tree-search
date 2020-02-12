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
