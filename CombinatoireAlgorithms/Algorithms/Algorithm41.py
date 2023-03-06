import numpy as np

def incindence_to_abjacency(incindence_matrix):
    rows = len(incindence_matrix)
    columns = len(incindence_matrix[0])
    abjacency_matrix = np.zeros((columns, columns))
    for v in range(rows):
        for e1 in range(columns-1):
            if(incindence_matrix[v][e1]):
                 for e2 in range(e1+1, columns):
                     if(incindence_matrix[e2][v]):
                         abjacency_matrix[v][e2] = 1
                         abjacency_matrix[e2][v] = 1

    return abjacency_matrix

A = np.array([
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1]
])

print(incindence_to_abjacency(A))