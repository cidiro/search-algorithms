from abc import ABC, abstractmethod
from utils.string_side_by_side import string_side_by_side
from utils.print_update import print_update
import threading
import time


class Strategy(ABC):
    def __init__(self):
        self.in_progress = False
        self.has_heuristic = False
        self.watch_node = None  # Current node
        self.seen_nodes = set()
        self.monitor_thread = threading.Thread(target=self.monitor,
                                               daemon=True)

    @abstractmethod
    def solve(self, start_state, is_goal_state, produce_new_states):
        pass

    def start(self, start_state, is_goal_state, produce_new_states):
        self.in_progress = True
        self.monitor_thread.start()
        solution = self.solve(start_state, is_goal_state, produce_new_states)
        self.in_progress = False
        return solution

    def monitor(self):
        start_time = time.time()
        while self.in_progress:
            elapsed_time = time.time() - start_time
            nodes_discovered = len(self.seen_nodes)
            state_lines = (str(self.watch_node.value).splitlines()
                           if self.watch_node else ["None"])

            if nodes_discovered:
                print_update(string_side_by_side(
                    f"{"Nodes discovered:":<18}{nodes_discovered}\n"
                    f"{"Time elapsed:":<18}{elapsed_time:.1f}s",
                    f"{"Current state:":<15}{state_lines[0]}\n"
                    f"{"\n".join([f"{"":<15}{line}"
                                  for line in state_lines[1:]])}",
                    column_width=26)
                )
            time.sleep(2)
