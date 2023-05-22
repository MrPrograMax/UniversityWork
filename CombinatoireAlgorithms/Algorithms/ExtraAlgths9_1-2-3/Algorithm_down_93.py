def down(k:int, j:int, C, L):
    """
    k - dimension and iterations
    j - insertion pointer
    return C,L
    Расщипляет j строку
    """
    #1
    beta   = C[j, : ]
    length = L[j]

    #2
    for i in range(j, k-2):
        C[i, :] = C[i+1, :]
        L[i]= L[i + 1]

    #3
    C[k-1, : ] = beta
    C[ k , : ] = beta

    #4
    C[k-1, length + 1] = 0
    C[k  , length + 1] = 1
    L[k-1] = length + 1
    L[ k ] = length + 1

    return C, L
