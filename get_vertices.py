import timeit
import time


def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)


# Пример использования
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]
start = 7
end = 2

time_start = timeit.default_timer()
print("The start time for count_vertices is :", time_start)
time.sleep(1)

get_vertices(edges)

print("The difference of time is :", timeit.default_timer() - time_start - 1)