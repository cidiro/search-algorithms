# from algorithms.breadth_first_search import BreadthFirstSearch
from algorithms.depth_first_search import DepthFirstSearch
from algorithms.solver import Solver
from algorithms.strategy import Strategy
from puzzles.puzzle import Puzzle
from puzzles.state import State as BaseState


class State(BaseState):
    def __init__(self, data: list[list[str]]):
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.data == other.data

    def __hash__(self):
        return hash(tuple(map(tuple, self.data)))

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.data])

    def __len__(self):
        return len(self.data)


class KnightsTour(Puzzle):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elapsed_time = 0
        self.path = None

        # Default initial state
        # ['O', 'O', 'O', 'O', 'O']
        # ['O', 'K', 'O', 'O', 'O']
        # ['O', 'O', 'O', 'O', 'O']
        # ['O', 'O', 'O', 'O', 'O']
        # ['O', 'O', 'O', 'O', 'O']
        self.initial_state = State(
            [['O' for _ in range(width)] for _ in range(height)]
        )
        self.initial_state.data[1][1] = 'K'

    def is_goal_state(self, state: State):
        for row in state.data:
            for cell in row:
                if cell == 'O':
                    return False
        return True

    def produce_new_states(self, state: State):
        valid_moves = []
        knight_position = self.get_knight_position(state)
        if knight_position is None:
            raise ValueError("Knight not found")
        else:
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            # moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
            #          (-2, -1), (-1, -2), (1, -2), (2, -1)]
            possible_moves = [
                (knight_position[0] + x, knight_position[1] + y)
                for x, y in moves
            ]
            valid_moves = [
                move for move in possible_moves
                if (self.is_within_bounds(move)
                    and state.data[move[0]][move[1]] == 'O')
            ]

        new_states = []

        for move in valid_moves:
            new_state = State([row.copy() for row in state.data])
            new_state.data[move[0]][move[1]] = 'K'
            new_state.data[knight_position[0]][knight_position[1]] = 'X'
            new_states.append(new_state)

        return new_states

    def solve(self, strategy: Strategy):
        solver = Solver(strategy)
        self.path = solver.solve(self.initial_state,
                                 self.is_goal_state,
                                 self.produce_new_states)
        self.elapsed_time = solver.elapsed_time

    def print_path(self):
        if self.path:
            for i, state in enumerate(self.path):
                if i != len(self.path) - 1:
                    print(f"{state}\n  |")
                else:
                    print(state)
            print(f"Path length: {len(self.path) - 1} moves")
        else:
            print("No path found")

    def get_knight_position(self, state: State):
        for i, row in enumerate(state.data):
            for j, cell in enumerate(row):
                if cell == 'K':
                    return i, j
        return None

    def is_within_bounds(self, position):
        return (0 <= position[0] < self.height
                and 0 <= position[1] < self.width)


def knights_tour(width=5, height=5):
    puzzle = KnightsTour(width, height)
    puzzle.solve(DepthFirstSearch())
    puzzle.print_path()
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
