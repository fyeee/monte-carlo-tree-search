import math
import random


class Node:
    c = 0.1

    def __init__(self, state, parent=None):
        self.state = state
        self.children = []
        self.parent = parent
        self.visits = 0
        self.reward = 0
        self.unexplored = [self.state.available_moves()]

    def is_leaf(self):
        return self.state.is_terminal()

    def get_UCT(self):
        return (self.reward / self.visits) + self.c * math.sqrt((math.log(self.parent.visit) / self.visits))

    def add_child(self, node):
        self.children.append(node)

    def fully_expanded(self):
        return len(self.state.available_moves()) == len(self.children)

    def random_child(self):
        node = Node(self.state.make_move(self.state.pick_random_move()), self)
        self.add_child(node)
        return node

    def is_terminal(self):
        return self.children == []

    def get_best_child(self):
        max_UCT = float("-inf")
        best_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            else:
                if child.get_UCT() > max_UCT:
                    max_UCT = child.get_UCT()
                    best_child = child
        return best_child
