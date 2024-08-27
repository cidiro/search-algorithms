from puzzles.graph_path import graph_path
from data.planets_graph import planets_graph

if __name__ == '__main__':
    graph = planets_graph()

    graph_path(graph, "Mars", "Pluto")
    graph.visualize()
