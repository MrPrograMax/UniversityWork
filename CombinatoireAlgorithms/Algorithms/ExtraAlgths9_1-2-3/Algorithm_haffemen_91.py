"""
Алгоритм Хаффмена
"""
import numpy as np

from Algorithm_wst_92 import wst
from Algorithm_down_93 import down

p1 = [0.4, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
p2 = [0.3, 0.2, 0.2, 0.2, 0.1]

def haffman(P:list, k : int = 2):
    """
    P  - массив вероятностей (по убыванию)
    k - количество букв анализируемого алфавита
    """
    c = np.array((k, k))
    L = np.zeros( k )
    if k == 2:
        c[0][0] = 0
        c[1][0] = 1
        L[0] = 1
        L[1] = 1
    else:
        delta = P[k-1] + P[k]
        j =  wst(k, delta, P)
        down(k, j)
