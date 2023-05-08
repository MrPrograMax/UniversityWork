import numpy as np

def Dijkstra_alg(graph, begin, end):
    n = len(graph[0])
    distance = np.zeros(n)
    visited = np.zeros(n)
    path = np.zeros(n)

    for i in range(n):
        distance[i] = np.inf

    distance[begin] = 0
    for i in range(n-1):
        min = np.inf
        # Из ещё не посещенных вершин находим вершину, имеющую минммальную метку
        for j in range(n):
            if not visited[i] and distance[i] <= min:
                min = distance[i]
                index = i # Сохраняем индекс вершины
        visited[index] = True # Помечаем, как посещенную
        for k in range(n):
            # Для каждого соседа найденной вершины, кроме отмеченных как посещённые,
            # рассмотрим новую длину пути, равную сумме значений текущей метки и длины ребра, соединяющего её с соседом.
            if not visited[k] and graph[index][k] != 0 and distance[index] != np.inf and (distance[index] + graph[index][k] < distance[k]):
                distance[k] = distance[index] + graph[index][k] # Заменяем значение метки

    print('Длина пути = ', end = "")
   
    if distance[end] != np.inf:
        print(distance[end])
    else:
        print('маршрут недоступен')

    if distance[end] == np.inf:
        return
    k = 0
    path[0] = end
    weight = distance[end]
    m = end

    while(end != begin): # Пока не дошли до начальной вершины
        for i in range(n):
            if graph[i][end] != np.inf and graph[i][end] != 0:  # Если связь есть
                temp = weight - graph[i][end] # Определяем вес пути из предыдущей вершины
                if temp == distance[i]: # Если вес совпал с расчитанным, значит из этой вершины и был переход
                    weight = temp # Сохраняем новый вес
                    end = i # Сохраняем прндыдущую вершины
                    path[k] = i # Записываем ее в массив
                    k += 1

    print(f'Минимальной путь из {begin} в {m} с помощью алгоритма Дийкстры')
    for i in range(k-1, -1, -1):
        print(int(path[i]), end = " -> ")
    print(m)

def floyd(W, start_point: int = 0, end_point: int = None) -> tuple:
    """ Возвращает минимальный путь и дистанцию 
        returning (path:list, distance:int)

        W - Начальные веса
        D - Дистанции
        H - Таблица кратчайших предшестующих точек
    """
    if end_point is None:
        end_point = W[0].size-1

    D = W.copy()
    n = len(W[0])
    H = np.zeros((n, n))

    error_flag = False
    # 1 Инициализация H
    for i in range(n):
        for j in range(n):
            if W[i][j] != np.inf and i != j:
                H[i][j] = i

    for k in range(n):
        # 2 Построение Н, D
        for i in range(n):
            for j in range(n):
                if k not in (i, j):
                    if D[i][k] != np.inf and D[k][j] != np.inf:
                        D[i][j] = min(D[i][j], D[i][k] + D[k][j])

                        if D[i][k] + D[k][j] <= D[i][j]:
                            H[i][j] = H[k][j]

        # 3 Проверка на окончание
        for i in range(n):
            if D[i][i] < 0:
                error_flag = True
                break

    # 7.4 Нахождение пути из Н

    if error_flag is False and D[start_point, end_point] != np.inf:
        point = end_point
        result_chain = [point]

        while point != start_point:
            point = int(H[start_point][point])

            result_chain.append(point)

        return np.flip(result_chain), D[start_point, end_point]

    else:
        print("Решения нет")
        return None, None

inf = np.inf
A = np.array([
    [0, 2, 1, 3, inf, 9, inf, inf],
    [inf, 0, inf, 3, 5, inf, inf, inf],
    [inf, inf, 0, inf, 1, 7, inf, inf],
    [inf, inf, inf, 0, 2, 2, inf, inf],
    [inf, inf, inf, inf, 0, inf, 3, inf],
    [inf, inf, inf, inf, inf, 0, 2, 2],
    [inf, inf, inf, inf, inf, inf, 0, 1],
    [inf, inf, inf, inf, inf, inf, inf, 0]
])


Dijkstra_alg(A, 0, 7)

print(f'Минимальный путь {0} -> {7} с помощью алгоритма Флойда')
chain, distance = floyd(A)

if chain is None:
    print("Пути нет")
else:
    print(" -> ".join(chain.astype(str)))
    print('Длина пути = ' + str(distance)
            if distance != np.inf
            else 'Маршрут недоступен')
