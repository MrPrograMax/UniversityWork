from queue import Queue
import numpy as np

def breadth_search(abjacency_matrix, start_vertix):
    X = [0] * len(abjacency_matrix)
    que = Queue()
    que.put(start_vertix)
    X[start_vertix] = 1
    while que.qsize() != 0:
        u = que.get()
        print(u+1)
        for i in range(len(abjacency_matrix)):
            if abjacency_matrix[u][i] == 1:
                if X[i] == 0:
                    que.put(i)
                    X[i] = 1

A = np.array([
    [0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
])

breadth_search(A, 0)
