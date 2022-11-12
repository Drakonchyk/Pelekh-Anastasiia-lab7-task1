"""adding edges"""

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    first_edge = edge[0]
    second_edge = edge[1]

    if first_edge in graph:
        graph[first_edge].append(second_edge)
    else:
        graph.setdefault(first_edge, [second_edge])

    if second_edge in graph:
        graph[second_edge].append(first_edge)
    else:
        graph.setdefault(second_edge, [first_edge])

    return graph


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
