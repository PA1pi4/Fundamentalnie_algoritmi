import heapq
import timeit
import time

def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(start, 0)]  # Приоритетная очередь (куча) 1 5  2 3

    while priority_queue:
        current_vertex, current_distance = heapq.heappop(priority_queue)  # 0 0

        # Если текущее расстояние больше известного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex]:  # 1 5  2 3
            distance = current_distance + weight  # et1: 0 + 5 = 5  0 + 3 = 3
            if distance < distances[neighbor]:  # et1: 5 < inf 3 < inf
                distances[neighbor] = distance  # et1: = 5  = 3
                heapq.heappush(priority_queue, (neighbor, distance))

    return distances


# Пример использования

graph = {
    0: [(1, 5), (2, 3)],
    1: [(3, 3), (2, 1)],
    2: [(3, 1), (1, 1)],
    3: []
}

time_start = timeit.default_timer()
print("The start time for count_vertices is :", time_start)
time.sleep(1)

print(dijkstra(graph, 0))  # Вывод: {0: 0, 1: 1, 2: 3, 3: 4}

print("The difference of time is :", timeit.default_timer() - time_start - 1)