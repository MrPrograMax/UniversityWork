print("hello im alg51, but i dont warking yet! ")

import numpy as np
print("hello im alg51, but i dont warking yet!")

def depth_search(L):
    n = len(L)
    stack=[]

    for i in range(n):
        stack.append(i)
        x = [i]
        for j in range(n):
            if j not in x and :
                stack.append(j)
                x.append(j)

    return "Пока возвращять нечего, печальное зрелище"

Links = np.array([
    [0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
])
LN = [
    [1,2,4],
    [0,3,4],
    [0,4],
    [1,4],
    [0,1,2,3,4,5,6],
    [4,6],
    [4,5]
]
