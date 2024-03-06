from abc import ABC, abstractmethod
from utils.print_update import print_update
import threading
import time


class Strategy(ABC):
    def __init__(self):
        self.in_progress = False
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
            state_string = (self.watch_node.value
                            if self.watch_node else "None")

            if nodes_discovered:
                print_update(self.format_string(nodes_discovered,
                                                elapsed_time,
                                                state_string))
            time.sleep(2)

    def format_string(self, nodes_discovered, elapsed_time, state):
        lines = str(state).split("\n")
        return (
            f"Nodes discovered: {nodes_discovered}\n"
            f"Time elapsed: {elapsed_time:.1f}s\n"
            f"{"\n".join([f"\t\t\t{line}" for line in lines[:-1]])}\n"
            f"Current state:\t\t{lines[-1]}"
        )
