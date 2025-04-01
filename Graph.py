Grapf = [[0,1], [0,2], [0,3], [2,3], [4,5], [1, 6]]

def search_connection(a, b, graph):
    start = a
    end = b
    matrixOfConnections = initialize_matrix(count_nodes(graph)[1])
    level = 1
    current_node = 0
    nodes = count_nodes(graph)[0]
    for node in nodes:
        level = 1
        for i in nodes:
            if edge_exsist(current_node, i, graph):
                if current_node == i:
                    continue
                matrixOfConnections[current_node][i] = level + 1
        level += 1
        current_node += 1

    return matrixOfConnections

def count_nodes(graph):
    amount_of_nodes = list(set([i for l in graph for i in l]))
    return amount_of_nodes, len(amount_of_nodes) # в amount_of_nodes соответствие номеров узлов по факту инедексам(номинальный номер узла)

def edge_exsist(current_node, next_node, graph):
    for i in graph:
        if (current_node in i) and (next_node in i):
            return True
        else:
            continue
    return False

def initialize_matrix(amount_of_nodes):
    matrix = []
    for i in range(amount_of_nodes):
        array = [0 for _ in range(amount_of_nodes)]
        array[i] = 1
        matrix.append(array)
    return matrix

for i in search_connection(1, 2, Grapf):
    print(i)