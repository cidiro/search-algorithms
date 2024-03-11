from algorithms.breadth_first_search import BreadthFirstSearch
# from algorithms.depth_first_search import DepthFirstSearch
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
        return '\n'.join([' '.join(row) for row in self.data])

    def __len__(self):
        return len(self.data)


class MadagascarCheckers(Puzzle):
    def __init__(self):
        super().__init__()
        self.width = 7
        self.height = 7

        # Default initial state
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        # ['x', 'x', '-', '*',, '-', 'x', 'x']
        # ['-', '-', '*', '*',, '*', '-', '-']
        # ['-', '-', '-', '*',, '-', '-', '-']
        # ['-', '-', '-', '*',, '-', '-', '-']
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        self.initial_state = State(
            [['-' for _ in range(self.width)] for _ in range(self.height)]
        )

        for i in range(2):
            for j in range(2):
                data = self.initial_state.data
                data[i][j] = 'x'
                data[i][self.width - 1 - j] = 'x'
                data[self.height - 1 - i][j] = 'x'
                data[self.height - 1 - i][self.width - 1 - j] = 'x'

        # Initial placement of the pieces
        self.initial_state.data[1][3] = '*'
        self.initial_state.data[2][2] = '*'
        self.initial_state.data[2][3] = '*'
        self.initial_state.data[2][4] = '*'
        self.initial_state.data[3][3] = '*'
        self.initial_state.data[4][3] = '*'

        # Goal state:
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        # ['-', '-', '-', '-',, '-', '-', '-']
        # ['-', '-', '-', '*',, '-', '-', '-']
        # ['-', '-', '-', '-',, '-', '-', '-']
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        # ['x', 'x', '-', '-',, '-', 'x', 'x']
        self.goal_state = State(
            [['-' for _ in range(self.width)] for _ in range(self.height)]
        )
        for i in range(2):
            for j in range(2):
                data = self.goal_state.data
                data[i][j] = 'x'
                data[i][self.width - 1 - j] = 'x'
                data[self.height - 1 - i][j] = 'x'
                data[self.height - 1 - i][self.width - 1 - j] = 'x'

        self.goal_state.data[3][3] = '*'

    def is_goal_state(self, state: State):
        return state == self.goal_state

    def produce_new_states(self, state: State):
        valid_moves = self.get_valid_moves(state)

        new_states = []
        for move in valid_moves:
            new_state = State([row.copy() for row in state.data])
            new_state.data[move[0][0]][move[0][1]] = '-'
            new_state.data[move[1][0]][move[1][1]] = '-'
            new_state.data[move[2][0]][move[2][1]] = '*'
            new_states.append(new_state)

        return new_states

    def get_valid_moves(self, state: State):
        valid_moves = []
        for i in range(self.height):
            for j in range(self.width):
                if state.data[i][j] == '*':
                    pos = (i, j)
                    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        jump_pos = (pos[0] + x, pos[1] + y)
                        x = x + 1 if x > 0 else x - 1 if x < 0 else x
                        y = y + 1 if y > 0 else y - 1 if y < 0 else y
                        move_pos = (pos[0] + x, pos[1] + y)
                        if (self.is_within_bounds(move_pos)
                            and state.data[move_pos[0]][move_pos[1]] == '-'):

                            if state.data[jump_pos[0]][jump_pos[1]] == '*':
                                valid_moves.append((pos, jump_pos, move_pos))

        return valid_moves

    def is_within_bounds(self, position):
        return (0 <= position[0] < self.height
                and 0 <= position[1] < self.width)


def madagascar_checkers():
    puzzle = MadagascarCheckers()
    puzzle.solve(BreadthFirstSearch())
    puzzle.print_path()
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
