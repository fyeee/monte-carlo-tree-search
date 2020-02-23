import random
from Node import Node
from FiveInRowState import FiveInRowState
from ast import literal_eval as make_tuple

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
        move = node.random_unexplored_move()
        child_state = node.state.make_move(move)
        expand_node = Node(child_state, node)
        node.add_child(expand_node)
        return expand_node

    def rollout(self, node):
        while not node.is_terminal():
            node = node.random_child()
        return node.state.get_reward()

    def backpropagation(self, node, reward):
        while node:
            node.visits += 1
            node.reward += reward
            node = node.parent

    def search(self):
        for i in range(1000):
            node = self.selection()
            node = self.expansion(node)
            reward = self.rollout(node)
            self.backpropagation(node, reward)
        return self.root.get_best_child()


if __name__ == "__main__":
    state = FiveInRowState(size=5)
    print(state)
    while True:
        move = make_tuple(input("Enter your move in the form (row, column): "))
        state = state.make_move(move)
        print(state)
        root = Node(state)
        search = MonteCarloTreeSearch(root)
        child = search.search()
        state = child.state
        print(child.state)
        # state = child.state.make_move((3,4))
        # root = Node(state)
        # search = MonteCarloTreeSearch(root)
        # child = search.search()
        # print(child.state)
        # state = child.state.make_move((3, 5))
        # root = Node(state)
        # search = MonteCarloTreeSearch(root)
        # child = search.search()
        # print(child.state)
        # state = child.state.make_move((3, 6))
        # root = Node(state)
        # search = MonteCarloTreeSearch(root)
        # child = search.search()
        # print(child.state)
