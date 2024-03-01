from algorithms.strategy import Strategy


class Solver:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def solve(self, start_state, end_state, produce_new_states):
        return self.strategy.solve(start_state,
                                   end_state,
                                   produce_new_states)
