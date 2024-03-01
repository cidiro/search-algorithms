from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def solve(self, start_state, end_state, produce_new_states):
        pass
