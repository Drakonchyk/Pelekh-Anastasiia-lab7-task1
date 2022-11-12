"""get graph coords from a file"""
def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file('data1.txt')
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        list_coords = []
        for line in file:
            list_coords.append([int(line[0]), int(line[2])])
    return list_coords


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


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph:
        if edge[1] in graph[edge[0]]:
            return True
    return False


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

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    >>> del_edge(({1: [2], 2: [1]}, (1, 3)))

    >>> del_edge(({1: [2], 2: [1]}, (3, 1)))

    >>> del_edge(({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 5)))
    """

    first_edge = edge[0]
    second_edge = edge[1]

    if first_edge in graph and second_edge in graph[first_edge]:
        graph[first_edge].remove(second_edge)

    if second_edge in graph and first_edge in graph[second_edge]:
        graph[second_edge].remove(first_edge)

    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph.setdefault(node, [])
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        del graph[node]
        for key in graph:
            if node in graph[key]:
                graph[key].remove(node)
    return graph

def convert_to_dot(graph):
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    >>> convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})
    """
    with open('graph.dot', 'w', encoding='utf-8') as file:
        file.write("graph{\n")
        for key in graph:
            for value in graph[key]:
                file.write(str(key) + "--" + str(value) + "\n")
        file.write("}")


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    is_edge_in_graph({1: [2], 2: [1], 3: [4], 4: [3], 6: [7], 7: [6]}, (5, 1))
