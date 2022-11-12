"""deleting an edge"""

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    first_edge = edge[0]
    second_edge = edge[1]

    if first_edge in graph:
        graph[first_edge].remove(second_edge)

    if second_edge in graph:
        graph[second_edge].remove(first_edge)

    return graph

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
