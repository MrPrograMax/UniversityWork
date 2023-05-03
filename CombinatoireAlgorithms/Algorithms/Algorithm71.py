import sys
import numpy as np

def Dijkstra_alg(graph, begin, end):
    n = len(graph[0])
    distance = np.zeros(n)
    visited = np.zeros(n)
    path = np.zeros(n)

    for i in range(n):
        distance[i] = sys.maxsize

    distance[begin] = 0
    for i in range(n-1):
        min = sys.maxsize
        # Из ещё не посещенных вершин находим вершину, имеющую минммальную метку
        for j in range(n):
            if not visited[i] and distance[i] <= min:
                min = distance[i]
                index = i # Сохраняем индекс вершины
        visited[index] = True # Помечаем, как посещенную
        for k in range(n):
            # Для каждого соседа найденной вершины, кроме отмеченных как посещённые,
            # рассмотрим новую длину пути, равную сумме значений текущей метки и длины ребра, соединяющего её с соседом.
            if not visited[k] and graph[index][k] != 0 and distance[index] != sys.maxsize and (distance[index] + graph[index][k] < distance[k]):
                distance[k] = distance[index] + graph[index][k] # Заменяем значение метки

    print(f'Длина пути из {begin} вершины до остальных')
    for i in range(n):
        if distance[i] != sys.maxsize:
            print(f'Из {begin} в {i} = {distance[i]}')
        else:
            print(f'Из {begin} в {i} маршрут недоступен')

    if distance[end] == sys.maxsize:
        return
    k = 0
    path[0] = end
    weight = distance[end]
    m = end

    while(end != begin): # Пока не дошли до начальной вершины
        for i in range(n):
            if graph[i][end] != sys.maxsize and graph[i][end] != 0:  # Если связь есть
                temp = weight - graph[i][end] # Определяем вес пути из предыдущей вершины
                if temp == distance[i]: # Если вес совпал с расчитанным, значит из этой вершины и был переход
                    weight = temp # Сохраняем новый вес
                    end = i # Сохраняем прндыдущую вершины
                    path[k] = i # Записываем ее в массив
                    k += 1

    print(f'Путь минимальной длины из {begin} в {m}')
    for i in range(k-1, -1, -1):
        print(int(path[i]), sep = "->")

A = np.array([
    [0, 2, 1, 3, sys.maxsize, 9, sys.maxsize, sys.maxsize],
    [sys.maxsize, 0, sys.maxsize, 3, 5, sys.maxsize, sys.maxsize, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, sys.maxsize, 1, 7, sys.maxsize, sys.maxsize],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0, 2, 2, sys.maxsize, sys.maxsize],
    [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0, 2, 2],
    [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize,sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize,sys.maxsize,sys.maxsize , 0]
])

Dijkstra_alg(A, 0, 7)