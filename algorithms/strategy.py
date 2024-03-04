from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def solve(self, start_state, is_goal_state, produce_new_states):
        pass
