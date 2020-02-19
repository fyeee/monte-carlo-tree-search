from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def pick_random_move(self):
        pass

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def make_move(self, move):
        pass

    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def get_reward(self):
        pass
