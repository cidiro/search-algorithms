# from algorithms.breadth_first_search import BreadthFirstSearch
# from algorithms.depth_first_search import DepthFirstSearch
from algorithms.uniform_cost_search import UniformCostSearch
from puzzles.puzzle import Puzzle
from puzzles.state import State as BaseState
from graph.graph import Graph


class State(BaseState):
    def __init__(self, data: str, cost=0):
        self.data = data
        self.cost = cost

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return self.data

    def __len__(self):
        return len(self.data)


class GraphPath(Puzzle):
    def __init__(self, graph: Graph, initial_value, goal_value):
        super().__init__()
        self.graph = graph
        self.initial_state = State(initial_value)
        self.goal_state = State(goal_value)

    def is_goal_state(self, state: State):
        return state == self.goal_state

    def produce_new_states(self, state: State):
        node = self.graph.get_node(state.data)
        return (
            [State(neighbor.value, self.graph.get_link(node, neighbor).value)
             for neighbor in node.get_neighbors()]
        )


def graph_path(graph: Graph, initial_value, goal_value):
    puzzle = GraphPath(graph, initial_value, goal_value)
    puzzle.solve(UniformCostSearch())
    puzzle.print_path()
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
