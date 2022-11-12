"""writing edges into a dictionary"""

def to_edge_dict(edge_list):
    """
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [3, 2], 5: [1]}
    """
    dictionary = {}

    for edge in edge_list:
        first_edge = edge[0]
        second_edge = edge[1]

        if first_edge in dictionary:
            dictionary[first_edge].append(second_edge)
        else:
            dictionary.setdefault(first_edge, [second_edge])

        if second_edge in dictionary:
            dictionary[second_edge].append(first_edge)
        else:
            dictionary.setdefault(second_edge, [first_edge])

    return dictionary


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
