def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file('D:\labs\lab7\Pelekh-Anastasiia-lab7-task1\data1.txt')
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        list_coords = []
        for line in file:
            list_coords.append([int(line[0]), int(line[2])])
    return list_coords

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
