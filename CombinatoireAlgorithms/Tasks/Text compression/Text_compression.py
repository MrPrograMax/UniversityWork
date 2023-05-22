import numpy as np

def down(k:int, j:int, C, L) -> tuple:
    """
    k - dimension and iterations
    j - insertion pointer
    C - massive n*n
    L - length set
    return C,L
    Расщипляет j строку
    """
    #1
    beta   = C[j, : ]
    length = L[j]

    #2
    for i in range(j, k-2):
        C[i, :] = C[i + 1, :]
        L[i]  = L[i + 1]

    #3
    C[k - 1, : ] = beta
    C[  k  , : ] = beta

    #4
    C[k - 1, length + 1] = 0
    C[  k  , length + 1] = 1
    L[k - 1] = length + 1
    L[  k  ] = length + 1

    return C, L

def wst(k:int, delta, probs:list):
    """
    k - count of iteration and dimension
    delta - the sum of the last two numbers
    prob - probabilities

    returns a pointer to where the insert was made
    """

    probs[k-1] = delta

    for i in range(k - 1, 1, -1):
        #от к-1 до 2 в обратном порядке
        if probs[i - 1] < probs[i]:
            probs[i - 1], probs[i] = probs[i], probs[i - 1]
        else:
            break

    return i, probs

def haffman(P:list, k : int = 2):
    """
    P  - массив вероятностей (по убыванию)
    k - количество букв анализируемого алфавита
    """
    C = np.array((k, k))
    L = np.zeros( k )
    if k == 2:
        C[0][0] = 0
        C[1][0] = 1
        L[0] = 1
        L[1] = 1
    else:
        delta = P[k-1] + P[k]
        j, P = wst(k, delta, P)
        C, L = down(k, j, C, L)

    return C, L

p1 = [0.4, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
p2 = [0.3, 0.2, 0.2, 0.2, 0.1]
