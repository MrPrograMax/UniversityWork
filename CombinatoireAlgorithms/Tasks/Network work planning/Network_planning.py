"""На основе модифицированного алгоритма Флойда для нахождения максимального пути"""


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
