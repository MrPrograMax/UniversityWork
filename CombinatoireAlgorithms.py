import sys
import numpy as np
import pandas as pd
import itertools as iter


# region Algorithms

# Alg 2.1
def GenerationOfNbitBinaryVectors(n, flagOnPrint=False):
    B = np.zeros(n)
    countOperation = 0
    while True:
        if IsContainsOnlyUnits(B):
            if flagOnPrint:
                print(f"B contains only units: B = {B}")
            break
        else:
            countOperation += 1
            if flagOnPrint:
                print(f"{countOperation}) Current B: {B}")
            m = -1
            for i in range(len(B)):
                if B[i] == 0:
                    m = i
            B[m] = 1
            for j in range(m + 1, n):
                B[j] = 0

    return countOperation


def IsContainsOnlyUnits(arr):
    for i in arr:
        if i != 1:
            return False

    return True


def GetInfoAboutBastMilitaryBase(numberOfAreas, neighborhoodMatrix, losses):
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

    print(f"Минимальная сумма: {minSum}\nРасположение баз: {indexBase}\nМинимальное кол-во баз: {len(indexBase)}")


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


# endregion

# region Tests

def TestAlg21(end):
    end += 1
    operations = []
    n = range(1, end)
    for i in range(1, end):
        operations.append(GenerationOfNbitBinaryVectors(i))

    data = pd.DataFrame(
        {
            'n': n,
            'operations': operations
        }
    )
    print(data)


# endregion

# region Main

TestAlg21(20)

A = np.array([
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1]
])


losses = [0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1, 0.1]
GetInfoAboutBastMilitaryBase(9, A, losses)

# endregion