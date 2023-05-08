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

    print('Длина пути = ' + str(distance[end]) if distance[end] != np.inf else f'Из {begin} в {end} маршрут недоступен')

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

    print(f'Минимальный путь {begin} -> {m} c помощью алгоритма Дийкстры')
    for i in range(k-1, -1, -1):
        print(int(path[i]), end = ' -> ')
    print(m)
    print()

def Floid_alg(W, begin:int, end:int):
    """ W - Начальные веса
        D - Дистанции
        H - Таблица кратчайших предшестующих точек
    """
    D = W.copy()
    n = len(W[0])
    H = np.zeros((n, n))

    error_flag = False
    #1 Инициализация H
    for i in range(n):
        for j in range(n):
            if W[i][j] != np.inf and i != j:
                H[i][j] = i

    k = -1
    while True:
        k += 1
        #2 Построение Н, D
        for i in range(n):
            for j in range(n):
                if k not in (i, j):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

                    if D[i,k] + D[k,j] <= D[i,j]:
                        H[i,j] = H[k,j]
                        
        #3 Проверка на окончание
        for i in range(n):
            if D[i][i] < 0:
                error_flag = True
                break
        if k == n-1:
            break
    #7.4 Нахождение пути из Н

    if(error_flag is False):   
        q = end
        print(f'Минимальный путь {begin} -> {end} с помощью алгоритма Флойда')
        print(q, end = '')
        while q != begin:
            q = int(H[begin][q])
            print(' <- ' + str(q), end = '')
        print()

        print('Длина пути = ' + str(D[begin, end]) if D[begin][end] != np.inf else f'Из {begin} в {end} маршрут недоступен')

    else:
        print("Решения нет")

inf = np.inf
A = np.array([
    [  0,    2,  1,   3, inf,   9, inf, inf],
    [inf,   0, inf,   3,   5, inf, inf, inf],
    [inf, inf,   0, inf,   1,   7, inf, inf],
    [inf, inf, inf,   0,   2,   2, inf, inf],
    [inf, inf, inf, inf,   0, inf,   3, inf],
    [inf, inf, inf, inf, inf,   0,   2,   2],
    [inf, inf, inf, inf, inf, inf,   0,   1],
    [inf, inf, inf, inf, inf, inf, inf,   0]
])


Dijkstra_alg(A, 0, 7)
Floid_alg(A, 0, 7)
