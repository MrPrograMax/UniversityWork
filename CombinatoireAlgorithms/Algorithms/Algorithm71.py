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

    print(f'Длина пути из {begin} вершины до остальных c помощью алгоритма Дейкстры')
    for i in range(n):
        if distance[i] != np.inf:
            print(f'Из {begin} в {i} = {distance[i]}')
        else:
            print(f'Из {begin} в {i} маршрут недоступен')

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

    print(f'Путь минимальной длины из {begin} в {m}')
    for i in range(k-1, -1, -1):
        print(int(path[i]), sep = "->")
    print(m)

def Floid_alg(graph, begin:int, end:int):
    distance = graph.copy()
    n = len(graph[0])
    H = np.zeros((n, n))
    k, count = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != np.inf:
                H[i][j] = i
    while True:
        k += 1
        for i in range(n):
            for j in range(n):
                #if i != k and j != k:
                  #  distance[i][j] = min(distance[i][j], (distance[i][k] + distance[k][j]))
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    H[i][j] = H[k][j]

        for i in range(n):
            if distance[i][i] < 0:
                print("Решения нет")
                break
            if distance[i][i] >= 0:
                count += 1

        if count == len(distance) and k == n-1:
            break
        count = 0

    print(f'Длина пути из {begin} вершины до остальных с помощью алгоритма Флойда')
    for i in range(n):
        if distance[begin][i] != np.inf:
            print(f'Из {begin} в {i} = {distance[begin][i]}')
        else:
            print(f'Из {begin} в {i} маршрут недоступен')

    '''
    q = int(begin)
    print(q)
    while q != end:
        print(q)
        q = int(H[q][end])
    print(end)
    '''

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
Floid_alg(A, 0, 7)
