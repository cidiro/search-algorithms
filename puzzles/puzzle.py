from abc import ABC, abstractmethod
from algorithms.strategy import Strategy

from puzzles.state import State


class Puzzle(ABC):
    @abstractmethod
    def is_goal_state(self, state: State):
        pass

    @abstractmethod
    def produce_new_states(self, state: State):
        pass

    @abstractmethod
    def solve(self, strategy: Strategy):
        pass
