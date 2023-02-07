import numpy as np


# region Maxim G.

# Alg 2.1

def GenerationOfNbitBinaryVectors(n):
    B = np.zeros(n)
    while True:
        if IsContainsOnlyUnit(B):
            print(f"B contains only unit: B = {B}")
            break
        else:
            print(f"Current B: {B}")
            m = -1
            for i in range(len(B)):
                if B[i] == 0:
                    m = i
            B[m] = 1
            for j in range(m + 1, n):
                B[j] = 0


def IsContainsOnlyUnit(arr):
    result = True
    for i in arr:
        if i != 1:
            return False

    return True



# endregion


# region Maxim D.


# endregion


# region Ruslan Z.


# endregion
