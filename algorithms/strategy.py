from abc import ABC, abstractmethod
import threading
import time


class Strategy(ABC):
    def __init__(self):
        self.seen_nodes = set()
        self.in_progress = False
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
        while True:
            if not self.in_progress:
                break
            print(f"\rTime elapsed: {(time.time() - start_time):.1f}s - "
                  f"Seen nodes: {len(self.seen_nodes)}", end='', flush=True)
            time.sleep(2)
