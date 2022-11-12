"""adding a node"""

def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph.setdefault(node, [])
    return graph

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
