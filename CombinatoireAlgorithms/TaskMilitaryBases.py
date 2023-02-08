import sys
import itertools as iter


def GetInfoAboutBastMilitaryBase(numberOfAreas, neighborhoodMatrix, losses):
    # asymptotic = Θ(n^3 * n!)
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

    print(f"Минимальная сумма: {minSum}\nРасположение баз: {indexBase}\nСоответствующее кол-во баз: {len(indexBase)}")


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