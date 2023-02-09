import numpy as np


def GenerationOfKElementSubsetsNElementSet(n, k):
    A = np.array(range(0, k + 1))
    p = k
    while True:
        PrintCurrentValue(A, p)
        if A[k] == n:
            p = p - 1
        else:
            p = k

        if p >= 1:
            for i in range(k, p - 1, -1):
                A[i] = A[p] + i - p + 1
        else:
            break


def PrintCurrentValue(A, p):
    A = np.delete(A, 0)
    print(f"Current value: {A}, P = {p}")


# Test from the example in the book-tutorial(учебник)
GenerationOfKElementSubsetsNElementSet(7, 5)



