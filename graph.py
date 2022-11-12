"""save a graph"""

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
