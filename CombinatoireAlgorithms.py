import numpy as np
import pandas as pd


# region Maxim G.

# Alg 2.1

def GenerationOfNbitBinaryVectors(n, flagOnPrint = False):
    B = np.zeros(n)
    countOperation = 0
    while True:
        if IsContainsOnlyUnit(B):
            if flagOnPrint:
                print(f"B contains only unit: B = {B}")
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


def IsContainsOnlyUnit(arr):
    for i in arr:
        if i != 1:
            return False

    return True


# Test count of operation:
def Test(end):
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


Test(20)
# endregion


# region Maxim D.


# endregion


# region Ruslan Z.


# endregion
