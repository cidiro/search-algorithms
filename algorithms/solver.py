from algorithms.strategy import Strategy
import time


class Solver:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.elapsed_time = 0

    def solve(self, start_state, is_goal_state, produce_new_states):
        start_time = time.time()
        solution = self.strategy.solve(start_state,
                                       is_goal_state,
                                       produce_new_states)

        self.elapsed_time = time.time() - start_time
        return solution
