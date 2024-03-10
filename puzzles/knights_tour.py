# from algorithms.breadth_first_search import BreadthFirstSearch
# from algorithms.depth_first_search import DepthFirstSearch
from algorithms.greedy_best_first_search import GreedyBestFirstSearch
from puzzles.puzzle import Puzzle
from puzzles.state import State as BaseState
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


class State(BaseState):
    def __init__(self, data: list[list[str]]):
        self.data = data
        self.heuristic = 0

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.data == other.data

    def __hash__(self):
        return hash(tuple(map(tuple, self.data)))

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.data])

    def __len__(self):
        return len(self.data)


class KnightsTour(Puzzle):
    def __init__(self, knight_row, knight_col, width, height):
        super().__init__()
        self.width = width
        self.height = height

        # Default initial state (5x5)
        # ['-', '-', '-', '-', '-']
        # ['-', 'K', '-', '-', '-']
        # ['-', '-', '-', '-', '-']
        # ['-', '-', '-', '-', '-']
        # ['-', '-', '-', '-', '-']
        self.initial_state = State(
            [['-' for _ in range(width)] for _ in range(height)]
        )
        self.initial_state.data[knight_row][knight_col] = 'K'

    def is_goal_state(self, state: State):
        for row in state.data:
            for cell in row:
                if cell == '-':
                    return False
        return True

    def produce_new_states(self, state: State):
        valid_moves = self.get_valid_moves(state)
        knight_position = self.get_knight_position(state)

        new_states = []
        for move in valid_moves:
            new_state = State([row.copy() for row in state.data])
            new_state.data[move[0]][move[1]] = 'K'
            new_state.data[knight_position[0]][knight_position[1]] = '*'
            new_state.heuristic = (self.calculate_heuristic(new_state)
                                   if self.strategy.has_heuristic else 0)
            new_states.append(new_state)

        return new_states

    def get_valid_moves(self, state: State):
        valid_moves = []
        knight_position = self.get_knight_position(state)
        if knight_position is None:
            raise ValueError("Knight not found")
        else:
            # moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                     (-2, -1), (-1, -2), (1, -2), (2, -1)]
            possible_moves = [
                (knight_position[0] + x, knight_position[1] + y)
                for x, y in moves
            ]
            valid_moves = [
                move for move in possible_moves
                if (self.is_within_bounds(move)
                    and state.data[move[0]][move[1]] == '-')
            ]
        return valid_moves

    def get_knight_position(self, state: State):
        for i, row in enumerate(state.data):
            for j, cell in enumerate(row):
                if cell == 'K':
                    return i, j
        return None

    def is_within_bounds(self, position):
        return (0 <= position[0] < self.height
                and 0 <= position[1] < self.width)

    def calculate_heuristic(self, state: State):
        return len(self.get_valid_moves(state))

    def plot_tour(self, stage):
        def plot_move(start, end):
            plt.plot([start[1], end[1]], [start[0], end[0]], 'k-', linewidth=2)
            plt.text(start[1], start[0], '★', fontsize=40,
                     ha='center', va='center', color='black')

        if self.path:
            if stage >= len(self.path):
                stage = len(self.path) - 1

            light_brown = "#ffdcb8"
            dark_brown = "#bf803b"

            plt.figure(figsize=(self.width, self.height))

            # Initialize the chessboard with colored squares
            chessboard_color = np.full((self.width, self.height, 3),
                                       np.array(mcolors.to_rgb(light_brown)))
            chessboard_color[1::2, ::2] = mcolors.to_rgb(dark_brown)
            chessboard_color[::2, 1::2] = mcolors.to_rgb(dark_brown)

            # Display the chessboard
            plt.imshow(chessboard_color)

            for i in range(stage - 1):
                start = self.get_knight_position(self.path[i].value)
                end = self.get_knight_position(self.path[i + 1].value)
                plot_move(start, end)

            knight_pos = self.get_knight_position(self.path[stage].value)
            plot_move(self.get_knight_position(self.path[stage - 1].value),
                      knight_pos)

            plt.text(knight_pos[1], knight_pos[0], '♞',
                     fontsize=40, ha='center', va='center',
                     color='black', fontweight='bold')

            plt.title(f"Knight's Tour ({stage} moves)")
            plt.get_current_fig_manager().window.resizable(False, False)
            plt.axis('off')
            plt.show()


def knights_tour(knight_row=1, knight_col=1, width=5, height=5):
    puzzle = KnightsTour(knight_row, knight_col, width, height)
    puzzle.solve(GreedyBestFirstSearch())
    # puzzle.print_path()
    puzzle.plot_tour(25)
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
