# from puzzles.knights_tour import knights_tour
# from puzzles.string_arrange import string_arrange
from algorithms.breadth_first_search import BreadthFirstSearch
from puzzles.madagascar_checkers import MadagascarCheckers
# from test import draw_chessboard

if __name__ == '__main__':
    # string_arrange("olhel", "hello")
    # string_arrange("eningami", "imaginen")

    # knights_tour(1, 1, 8, 8)

    puzzle = MadagascarCheckers()
    puzzle.solve(BreadthFirstSearch())
    puzzle.print_path()
    print(f"Elapsed time: {puzzle.elapsed_time:.6f} seconds")
