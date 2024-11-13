from graphviz import Digraph


def create_bst(name, nodes, edges):
    dot = Digraph(name)
    dot.attr(rankdir='TB')

    # Add nodes
    for node in nodes:
        dot.node(node, node)

    # Add edges
    for edge in edges:
        dot.edge(edge[0], edge[1])

    return dot


# Initial Tree
def draw_initial_tree():
    nodes = ['H', 'B', 'I', 'A', 'G', 'K', 'E', 'J', 'L', 'C', 'F', 'N', 'D', 'M', 'O']
    edges = [
        ('H', 'B'), ('H', 'I'),
        ('B', 'A'), ('B', 'G'),
        ('G', 'E'),
        ('E', 'C'), ('E', 'F'),
        ('C', 'D'),
        ('I', 'K'),
        ('K', 'J'), ('K', 'L'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("Initial_Tree", nodes, edges)


# After deleting I
def draw_after_I():
    nodes = ['H', 'B', 'K', 'A', 'G', 'J', 'L', 'E', 'C', 'F', 'N', 'D', 'M', 'O']
    edges = [
        ('H', 'B'), ('H', 'K'),
        ('B', 'A'), ('B', 'G'),
        ('G', 'E'),
        ('E', 'C'), ('E', 'F'),
        ('C', 'D'),
        ('K', 'J'), ('K', 'L'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("After_I", nodes, edges)


# After deleting G
def draw_after_G():
    nodes = ['H', 'B', 'K', 'A', 'E', 'J', 'L', 'C', 'F', 'N', 'D', 'M', 'O']
    edges = [
        ('H', 'B'), ('H', 'K'),
        ('B', 'A'), ('B', 'E'),
        ('E', 'C'), ('E', 'F'),
        ('C', 'D'),
        ('K', 'J'), ('K', 'L'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("After_G", nodes, edges)


# After deleting K
def draw_after_K():
    nodes = ['H', 'B', 'J', 'A', 'E', 'L', 'C', 'F', 'N', 'D', 'M', 'O']
    edges = [
        ('H', 'B'), ('H', 'J'),
        ('B', 'A'), ('B', 'E'),
        ('E', 'C'), ('E', 'F'),
        ('C', 'D'),
        ('J', 'L'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("After_K", nodes, edges)


# After deleting B
def draw_after_B():
    nodes = ['H', 'C', 'J', 'A', 'E', 'L', 'D', 'F', 'N', 'M', 'O']
    edges = [
        ('H', 'C'), ('H', 'J'),
        ('C', 'A'), ('C', 'E'),
        ('E', 'D'), ('E', 'F'),
        ('J', 'L'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("After_B", nodes, edges)


# Final Tree (After deleting H)
def draw_final_tree():
    nodes = ['J', 'C', 'L', 'A', 'E', 'N', 'D', 'F', 'M', 'O']
    edges = [
        ('J', 'C'), ('J', 'L'),
        ('C', 'A'), ('C', 'E'),
        ('E', 'D'), ('E', 'F'),
        ('L', 'N'),
        ('N', 'M'), ('N', 'O')
    ]
    return create_bst("Final_Tree", nodes, edges)


# Generate all diagrams
trees = [
    draw_initial_tree(),
    draw_after_I(),
    draw_after_G(),
    draw_after_K(),
    draw_after_B(),
    draw_final_tree()
]

# Save each diagram
for i, tree in enumerate(trees):
    tree.render(f'bst_step_{i}', format='png', cleanup=True)