import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from graph.tree import Tree


def test_tree():
    tree = Tree('a')
    tree.add_node(tree.root, 'b')
    tree.add_node(tree.root, 'c')
    tree.add_node(tree.root, 'd')

    for child in tree.root.get_children():
        tree.add_node(child, child.value + '1')
        test_node = tree.add_node(child, child.value + '2')

    print(tree.root)
    for child in tree.root.get_children():
        print(str(child) + " - parent: " + str(child.get_parent()))
        for grandchild in child.get_children():
            print(str(grandchild) + " - parent: "
                  + str(grandchild.get_parent()))

    print(tree.find_path(test_node))


# Code by ChatGPT (many prompts)
def draw_chessboard(knight_pos):
    def plot_move(start, end):
        plt.plot([start[1], end[1]], [start[0], end[0]], 'k-', linewidth=2)
        plt.text(start[1], start[0], '★', fontsize=40,
                 ha='center', va='center', color='black')

    light_brown = "#ffdcb8"
    dark_brown = "#bf803b"

    # Set up the window size
    plt.figure(figsize=(8, 8))

    # Initialize the chessboard with colored squares
    chessboard_color = np.full((8, 8, 3),
                               np.array(mcolors.to_rgb(light_brown)))
    chessboard_color[1::2, ::2] = mcolors.to_rgb(dark_brown)
    chessboard_color[::2, 1::2] = mcolors.to_rgb(dark_brown)

    # Display the chessboard
    plt.imshow(chessboard_color)

    # Plot the knight's position using the Unicode character
    plt.text(knight_pos[1], knight_pos[0], '♞', fontsize=40, ha='center',
             va='center', color='black', fontweight='bold')

    # Plot lines for knight moves
    moves = [(1, 1), (3, 2), (1, 3), (0, 5), (1, 7), (3, 6), (5, 5), (4, 3)]
    for i in range(len(moves) - 1):
        plot_move(moves[i], moves[i + 1])
    plot_move(moves[-1], knight_pos)

    plt.title('Chessboard')
    plt.get_current_fig_manager().window.resizable(False, False)
    plt.axis('off')  # Turn off the axis for better visualization
    plt.show()
