import timeit
import time

def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)


def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)


def wave_algorithm(edges, start, end):  # определение функции волнового алгоритма
    """Реализация волнового алгоритма."""

    vertices = get_vertices(edges)  # вершины = список вершин

    # Инициализация массива пройденных вершин
    visited = {v: 0 for v in vertices}  # словарь посещенных вершин, в котором каждому ключу из списка вершин,
    # изначально соответствует значение 0, означающее шаг, на которм эта ввершина было посещена {1: 0, 2: 0, 3: 0,
    # 4: 0, 5: 0, 6: 0, 7: 0}
    visited[start] = 1  # элементу словаря с ключем, равным параметру start, соответствует значение, равное 1 {1: 0,
    # 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1}

    # Инициализация массива предков для восстановления пути
    parent = {v: None for v in vertices}  # словарь предков, в котором каждому ключу из списка вершин, изначально
    # соответствует значение None {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}

    # Флаг для проверки, найдена ли конечная вершина
    found = False

    # Шаг волнового алгоритма
    step = 1

    while True:
        # Флаг для проверки, были ли найдены новые вершины на текущем шаге
        new_vertices_found = False

        # Проходим по всем вершинам, которые были посещены на предыдущем шаге
        for v in vertices:  # v принимает значения всех вершин: 1, 2, 3, 4, 5, 6, 7
            if visited[v] == step:  # если значение элемента словаря посещенных вершин с ключем, равным значению
                # вершины из списка вершин, равено значению шага волнового алгортма et1: visited[v] = 1[7] = 1 = step
                # Проходим по всем соседям текущей вершины
                for edge in edges:  # edge - кортеж (u, v) представляющий ребро
                    # Проверяем ребра, где v является началом ребра
                    if edge[0] == v and visited[edge[1]] == 0:  # Если ребро начинается в v и конец ребра еще не
                        # посещен et1: edge[0] == 7 => проверяем значение visited[edge[1]] это visited[5] == 0 - да
                        visited[edge[1]] = step + 1  # Помечаем соседнюю вершину как посещенную на следующем шаге
                        # et1: visited[edge[1]] это visited[5] = step + 1 = 1 + 1 = 2 => {1: 0, 2: 0, 3: 0, 4: 0,
                        # 5: 2, 6: 0, 7: 1}
                        parent[edge[1]] = v  # Запоминаем, что пришли в edge[1] (это 5) из v, то есть parent[5]
                        # принимает значение v = 7 => {1: None, 2: None, 3: None, 4: None, 5: 7, 6: None, 7: None}
                        new_vertices_found = True  # Флаг, что нашли новые вершины
                    if edge[1] == v and visited[edge[0]] == 0:  # Если ребро заканчивается в v и начало ребра еще не
                        # посещенованного графа et1: edge[1] == 7 => проверяем значение visited[edge[0]] это visited[
                        # 6] == 0 - да
                        visited[edge[0]] = step + 1  # Помечаем соседнюю вершину et1: visited[edge[0]] это visited[6]
                        # = step + 1 = 1 + 1 = 2 => {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1}
                        parent[edge[0]] = v  # Запоминаем родителя et1: parent[edge[0]] это parent[6] принимает
                        # значение v = 7 => {1: None, 2: None, 3: None, 4: None, 5: 7, 6: 7, 7: None}
                        new_vertices_found = True  # Флаг, что нашли новые вершины

        # Если конечная вершина найдена, выходим из цикла
        if visited[end] != 0:  # Если в словаре посещенных вершин значение для ключа исходной вернины не равно 0,
            # то есть было найдено на каком-то шаге
            found = True  # флаг о нахождении искомой вершины
            break  # выход из цикла

        # Если новые вершины не найдены, выходим из цикла
        if not new_vertices_found:  # если не были найлены новые вершины
            break  # выход из цикла

        step += 1

    # Восстановление пути
    if found:  # если найдено искомое значение
        path = []  # создаем массив путь
        current = end  # обозначем искомое значение как действующее
        while current is not None:  # пока действующее значение на не None
            path.append(current)  # добавляем к массиву путь действующее значение
            current = parent[current]  # перезаписываем действующее значение на значение словаря предков с ключем
            # действующего значения end = 2, parent = {..., 2: 1, 1: 6, 6: 7, 7: None}.
        path.reverse()  # перевораиваем массив путь
        return path, visited  # возвращаем массив путь и словарь посещенных вершин
    else:
        return None, visited  # иначе возвращаем словарь посещенных вершин
    
# Пример использования
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]
start = 7
end = 2

time_start = timeit.default_timer()
print("The start time for wave_algorithm is :", time_start)
time.sleep(1)

path, visited = wave_algorithm(edges, start, end)

print("The difference of time for wave_algorithm is :", timeit.default_timer() - time_start - 1)

if path:
    print(f"Кратчайший путь от {start} до {end}: {path}")
else:
    print(f"Путь от {start} до {end} не найден")

print("Шаги посещения вершин:", visited)