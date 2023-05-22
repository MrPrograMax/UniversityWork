"""Сжимание текста на основе алгоритма Хаффмана"""
import numpy as np

def down(k:int, j:int, matrix_c, length_p) -> tuple:
    """
    k - dimension and iterations
    j - insertion pointer
    C - massive n*n
    L - length set
    return C,L
    Расщипляет j строку
    """
    #1
    beta   = matrix_c[j, : ]
    length = length_p[j]

    #2
    for i in range(j, k-2):
        matrix_c[i, :] = matrix_c[i + 1, :]
        length_p[i]  = length_p[i + 1]

    #3
    matrix_c[k - 1, : ] = beta
    matrix_c[  k  , : ] = beta

    #4
    matrix_c[k - 1, length + 1] = 0
    matrix_c[  k  , length + 1] = 1
    length_p[k - 1] = length + 1
    length_p[  k  ] = length + 1

    return matrix_c, length_p

def wst(k:int, delta, probs:list) -> tuple:
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

def haffman(letters_p:list, k : int = 2) -> tuple:
    """
    P  - массив вероятностей (по убыванию)
    k - количество букв анализируемого алфавита
    """
    matrix_c = np.zeros((k, k))
    length_p = np.zeros( k )
    if k == 2:
        matrix_c[0][0] = 0
        matrix_c[1][0] = 1
        length_p[0] = 1
        length_p[1] = 1
    else:
        delta = letters_p[k-1] + letters_p[k]
        j, letters_p = wst(k, delta, letters_p)
        matrix_c, length_p = down(k, j, matrix_c, length_p)

    return matrix_c, length_p

p1 = [0.4, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
p2 = [0.3, 0.2, 0.2, 0.2, 0.1]

POEM = """я_помню_чудное_мгновенье:_
передо_мной_явилась_ты,_
как_мимолетное_виденье,_
как_гений_чистой_красоты.
"""

LENGTH_POEM = len(POEM)

alph = set(POEM[:])
alph.remove('\n')
alph = list(alph)

dic_letter = {letter: POEM.count(letter)/LENGTH_POEM for letter in alph}

letter_probability = list(dic_letter.values())
letter_probability.sort()

C, L = haffman(letter_probability, 2)

print(f'C=\n{C}')
print(f'L=\n{L}')
