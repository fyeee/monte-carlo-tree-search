import random


class MonteCarloTreeSearch:
    def __init__(self, root):
        self.root = root

    def selection(self):
        node = self.root
        while not node.is_terminal():
            if not node.fully_expanded():
                return node
            node = node.get_best_child()
        return node

    def expansion(self, node):
        move = random.choice(node.unexplored)
        expand_node = node.state.make_move(move)
        node.add_child(expand_node)
        return expand_node

    def rollout(self, node):
        while not node.is_leaf():
            node = node.random_child()
        return node.get_UCT()

    def backpropagation(self, node, reward):
        while node:
            node.visits += 1
            node.reward += reward
            node = node.parent

    def search(self):
        for i in range(10000):
            node = self.selection()
            node = self.expansion(node)
            reward = self.rollout(node)
            self.backpropagation(node, reward)
        return self.root.get_best_child()
