"""deleting a node"""

def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    del graph[node]
    for values in graph:
        if node in graph[values]:
            graph[values].remove(node)
    return graph

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
