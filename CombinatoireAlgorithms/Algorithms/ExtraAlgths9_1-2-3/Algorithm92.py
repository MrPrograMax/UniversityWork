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

    return i
