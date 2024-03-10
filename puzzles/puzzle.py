from abc import ABC, abstractmethod
from algorithms.strategy import Strategy
import time

from puzzles.state import State


class Puzzle(ABC):
    def __init__(self):
        self.strategy = None
        self.elapsed_time = 0
        self.path = None

    @abstractmethod
    def is_goal_state(self, state: State):
        pass

    @abstractmethod
    def produce_new_states(self, state: State):
        pass

    def solve(self, strategy: Strategy):
        self.strategy = strategy

        print("Solving puzzle...\n")
        start_time = time.time()
        self.path = strategy.start(self.initial_state,
                                   self.is_goal_state,
                                   self.produce_new_states)
        self.elapsed_time = time.time() - start_time

    def print_path(self):
        if self.path:
            print()
            for i, state in enumerate(self.path):
                if i != len(self.path) - 1:
                    print(f"{state}\n  |")
                else:
                    print(state)
            print(f"Path length: {len(self.path) - 1} moves")
        else:
            print("No path found")
