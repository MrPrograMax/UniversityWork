"""На основе модифицированного алгоритма Флойда для нахождения максимального пути"""
import numpy as np


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

    k = -1
    while True:
        k += 1
        # 2 Построение Н, D
        for i in range(n):
            for j in range(n):
                if k not in (i, j):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

                    if D[i][k] + D[k][j] <= D[i][j]:
                        H[i][j] = H[k][j]

        # 3 Проверка на окончание
        for i in range(n):
            if D[i][i] < 0:
                error_flag = True
                break
        if k == n-1:
            break
    # 7.4 Нахождение пути из Н

    if error_flag is False:
        print(H)
        point = end_point
        result_chain = [point]

        while point != start_point:
            point = int(H[start_point][point])
            result_chain.append(point)

        return np.flip(result_chain), D[start_point, end_point]

    else:
        print("Решения нет")
        return None, None

def floyd_critical(W, start_point: int = 0, end_point: int = None) -> tuple:
    """ Возвращает критический путь, дистанцию
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

    k = -1
    while True:
        k += 1
        # 2 Построение Н, D
        for i in range(n):
            for j in range(n):
                if k not in (i, j):
                    D[i][j] = max(D[i][j], D[i][k] + D[k][j])

                    if D[i][k] + D[k][j] >= D[i][j]:
                        H[i][j] = H[k][j]

        # 3 Проверка на окончание
        for i in range(n):
            if D[i][i] < 0:
                error_flag = True
                break
        if k == n-1:
            break
    # 7.4 Нахождение пути из Н

    if error_flag is False:
        result_chain = [end_point]
        point = end_point

        while point != start_point:
            point = int(H[start_point][point])
            result_chain.append(point)

        return np.flip(result_chain), D[start_point, end_point]

    else:
        print("Решения нет")
        return None, None


inf = np.inf
network_graph = {
    #      0    1    2    3    4    5    6    7    8    9   10   11   12   13
    0 : [  0,   5,   7,  10,  19, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    1 : [inf,   0,  16, inf, inf,   8,   9,  14, inf, inf, inf, inf, inf, inf],
    2 : [inf, inf,   0, inf, inf,  11, inf, inf, inf, inf, inf, inf, inf, inf],
    3 : [inf, inf, inf,   0,  11, inf, inf, inf, inf,  26,  30, inf, inf, inf],
    4 : [inf, inf, inf, inf,   0, inf, inf, inf, inf,   3, inf, inf, inf, inf],
    5 : [inf, inf, inf, inf, inf,   0, inf, inf, inf,  13, inf,  17, inf, inf],
    6 : [inf, inf, inf, inf, inf, inf,   0, inf,  30, inf, inf, inf, inf, inf],
    7 : [inf, inf, inf, inf, inf, inf, inf,   0,  18, inf, inf,  21, inf, inf],
    8 : [inf, inf, inf, inf, inf, inf, inf, inf,   0, inf, inf, inf,   8, inf],
    9 : [inf, inf, inf, inf, inf, inf, inf, inf, inf,   0,  15, inf, inf, inf],
    10: [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,   0, 19,   12, inf],
    11: [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,  0,   14, inf],
    12: [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,   0,   7],
    13: [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,   0]
}
network_array = np.array(list(network_graph.values()))
n = network_array[0].size

for i in range(n-1):
    for j in range(i+1, n):
        print(f'Минимальный путь {i} -> {j} с помощью алгоритма Флойда')
        chain, distance = floyd(network_array, i, j)

        if chain is None:
            print("Пути нет")
        else:
            print(" -> ".join(chain.astype(str)))
            print('Длина пути = ' + str(distance)
                    if distance != np.inf
                    else 'Маршрут недоступен')
        print()

print(f'\nКритический путь {0} -> {n} с помощью алгоритма Флойда')
chain, distance = floyd_critical(network_array)
if chain is None:
    print("Пути нет")
else:
    print(" -> ".join(chain.astype(str)))
    print('Длина пути = ' + str(distance)
            if distance != np.inf
            else 'Маршрут недоступен')
