import heapq


class WeightedGraph:  # Создаем класс "Взвешенный граф"
    def __init__(self):
        self.graph = {}

    def count_vertices(self):
        """Подсчет количества вершин в графе."""
        vertices = set()
        for vertex in self.graph:
            vertices.add(vertex)
        return len(vertices)

    def get_vertices(self):
        """Получение списка вершин из списка ребер."""
        vertices = set()
        for vertex in self.graph:
            vertices.add(vertex)
        return list(vertices)

    def get_edges(self):
        """Получение кортежного списка ребер."""
        edges = [(key, edge[0]) for key in graph for edge in graph[key]]
        return list(edges)

    def wave_algorithm(self, start, end):
        """Реализация волнового алгоритма."""

        vertices = WeightedGraph.get_vertices(self)  # вершины = список вершин (0, 1, 2, 3)

        # Инициализация словаря пройденных вершин
        visited = {vertex: 0 for vertex in vertices}  # словарь посещенных вершин, в котором каждому ключу из списка
        # вершин, изначально соответствует значение 0, означающее шаг, на которм эта ввершина было посещена {0:0,
        # 1: 0, 2: 0, 3: 0}
        visited[start] = 1  # элементу словаря с ключем, равным параметру start, соответствует значение, равное 1 {
        # 0:1, 1: 0, 2: 0, 3: 0}

        # Инициализация словаря предков для восстановления пути
        parent = {vertex: None for vertex in vertices}  # словарь предков, в котором каждому ключу из списка вершин,
        # изначально соответствует значение None {0: None, 1: None, 2: None, 3: None}

        # Флаг для проверки, найдена ли конечная вершина
        found = False

        # Шаг волнового алгоритма
        step = 1

        while True:
            # Флаг для проверки, были ли найдены новые вершины на текущем шаге
            new_vertices_found = False

            # Проходим по всем вершинам, которые были посещены на предыдущем шаге
            for vertex in vertices:  # v принимает значения всех вершин: 0, 1, 2, 3
                if visited[vertex] == step:  # если значение элемента словаря посещенных вершин с ключем, равным
                    # значению вершины из списка вершин, равено значению шага волнового алгортма et1: visited[vertex]
                    # = 1[0] = 1 = step
                    # Проходим по всем соседям текущей вершины
                    for edge in WeightedGraph.get_edges(self):
                        # Проверяем ребра, где v является началом ребра
                        if edge[0] == vertex and visited[edge[1]] == 0:  # Если ребро начинается в v и конец ребра
                            # еще не посещен et1: edge[0] == 7 => проверяем значение visited[edge[1]] это visited[5]
                            # == 0 - да
                            visited[edge[1]] = step + 1
                            parent[edge[1]] = vertex
                            new_vertices_found = True
                        if edge[1] == vertex and visited[edge[0]] == 0:
                            visited[edge[0]] = step + 1
                            parent[edge[0]] = vertex
                            new_vertices_found = True

            # Если конечная вершина найдена, выходим из цикла
            if visited[end] != 0:
                found = True
                break

            # Если новые вершины не найдены, выходим из цикла
            if not new_vertices_found:
                break

            step += 1

        # Восстановление пути
        if found:
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, visited
        else:
            return None, visited

    def dijkstra(self, start):
        # Инициализация расстояний
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # Приоритетная очередь (куча) et1: 1 5  2 3

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)  # et1: 0 0

            # Если текущее расстояние больше известного, пропускаем
            if current_distance > distances[current_vertex]:
                continue

            # Обновляем расстояния до соседей
            for neighbor, weight in self.graph[current_vertex]:  # et1: 1 5  2 3
                distance = current_distance + weight  # et1: 0 + 5 = 5  0 + 3 = 3
                if distance < distances[neighbor]:  # et1: 5 < inf 3 < inf
                    distances[neighbor] = distance  # et1: = 5  = 3
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Пример использования
graph = {
    0: [(1, 1), (2, 3)],
    1: [(3, 3), (2, 1)],
    2: [(3, 1), (1, 1)],
    3: []
}

# Создаем экземпляр графа
wg = WeightedGraph()
wg.graph = graph

# Тестируем методы
print("Количество вершин:", wg.count_vertices())
print("Список вершин:", wg.get_vertices())
print("Список ребер:", wg.get_edges())

start = 0
end = 3

path, visited = wg.wave_algorithm(start, end)

if path:
    print(f"Кратчайший путь от {start} до {end} (без учета весов): {path}")
else:
    print(f"Путь от {start} до {end} не найден")

print("Шаги посещения вершин:", visited)

print("Расстояния (Дейкстра):", wg.dijkstra(0))