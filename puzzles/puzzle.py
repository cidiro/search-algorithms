from abc import ABC, abstractmethod

from puzzles.state import State


class Puzzle(ABC):
    @abstractmethod
    def produce_new_states(self, state: State):
        pass

    @abstractmethod
    def solve(self):
        pass
