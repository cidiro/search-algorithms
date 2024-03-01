from graph.node import Node
from graph.tree import Tree


def test_tree():
    tree = Tree(Node('a'))
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
