import numpy as np


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
