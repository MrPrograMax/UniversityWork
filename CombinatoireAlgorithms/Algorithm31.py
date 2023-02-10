import numpy as np


def GenerationOfKElementSubsetsNElementSet(n, k):
    result = np.array([[]])
    A = np.array(range(0, k + 1))
    result = np.append(result, [GetGoodData(A)], axis=1)
    p = k
    while True:
        PrintCurrentValue(A, p)
        result = np.append(result, [GetGoodData(A)], axis=0)
        if A[k] == n:
            p = p - 1
        else:
            p = k

        if p >= 1:
            for i in range(k, p - 1, -1):
                A[i] = A[p] + i - p + 1
        else:
            break

    result = np.delete(result, 0, axis=0)
    return result


def PrintCurrentValue(A, p):
    A = np.delete(A, 0)
    print(f"Current value: {A}, P = {p}")


def GetGoodData(arr):
    arr = np.delete(arr, 0)
    for i in range(len(arr)):
        arr[i] -= 1
    return arr


# Test from the example in the book-tutorial(учебник)
a = GenerationOfKElementSubsetsNElementSet(7, 3)
