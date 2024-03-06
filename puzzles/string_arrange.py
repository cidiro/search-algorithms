from algorithms.breadth_first_search import BreadthFirstSearch
# from algorithms.depth_first_search import DepthFirstSearch
from puzzles.puzzle import Puzzle
from puzzles.state import State as BaseState


class State(BaseState):
    def __init__(self, data: str):
        self.data = list(data)

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.data == other.data

    def __hash__(self):
        return hash(tuple(self.data))

    def __str__(self):
        return ''.join(self.data)

    def __len__(self):
        return len(self.data)

    def copy(self):
        return State(''.join(self.data))

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


class StringArrange(Puzzle):
    def __init__(self, initial_string, final_string):
        super().__init__()
        self.initial_state = State(initial_string)
        self.final_state = State(final_string)

    def is_goal_state(self, state: State):
        return state == self.final_state

    def produce_new_states(self, state: State):
        new_states = []

        for i in range(len(state) - 1):
            new_state = state.copy()
            new_state.swap(i, i + 1)
            new_states.append(new_state)

        # Removing duplicates with a set and list comprehension
        # preserves order and is most efficient
        seen = set()
        new_states = [x for x in new_states if not (x in seen or seen.add(x))]

        return new_states


def string_arrange(initial_string, final_string):
    puzzle = StringArrange(initial_string, final_string)
    puzzle.solve(BreadthFirstSearch())
    puzzle.print_path()
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
