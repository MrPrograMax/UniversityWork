import sys
import itertools as iter
from time import perf_counter
import numpy as np

def GetInfoAboutBastMilitaryBase(numberOfAreas, neighborhoodMatrix, losses):
    # asymptotic = Θ(n^3 * n!)

    time_start = perf_counter() #timer

    if IsValid(numberOfAreas, neighborhoodMatrix, losses) == False:
        return 0

    minSum = sys.maxsize * 2 + 1  # int max value
    indexBase = []
    keys = range(numberOfAreas)

    for i in range(numberOfAreas, 1, -1):
        combinations = list(iter.combinations(keys, i))

        for curKeys in combinations:
            vector = GetSumOfVectors(neighborhoodMatrix, curKeys)
            if IsNoneZero(vector):
                sum = 0
                for k in curKeys:
                    sum += losses[k]
                if sum < minSum:
                    minSum = sum
                    indexBase = curKeys

    time_end = perf_counter() 
    print(f"Минимальная сумма: {minSum}\nРасположение баз: {indexBase}\nСоответствующее кол-во баз: {len(indexBase)}\nВремя работы: {time_end-time_start}")


def IsNoneZero(arr):
    for i in arr:
        if i == 0:
            return False

    return True


def GetSumOfVectors(arrays, keys):
    result = [0] * len(arrays)
    for i in keys:
        result += arrays[i]

    return result


def IsValid(numberOfAreas, Matrix, losses):
    """ numberOfAreas is n
        Matrix is A
        losses is c
    """

    if not isinstance(numberOfAreas, int):
        print(">> Ошибка! Код: 101: Размерность не является целочисленной")
        return False

    if not isinstance(Matrix, np.ndarray):
        print(">> Ошибка! Код: 202: Матрица не принадлежит классу numpy.ndarray")
        return False
    
    if numberOfAreas <= 0:
        print(">> Ошибка! Код: 102: Размерность нулевая или отрицательная")
        return False
    
    if numberOfAreas != len(Matrix):
        print(">> Ошибка! Код: 103: Размерность не соответствует колличеству векторов в матрице!")
        return False
    
    if numberOfAreas != len(losses):
        print(">> Ошибка! Код: 104: Размерность не соответствует колличеству элементов в векторе потерь!")
        return False

    return True