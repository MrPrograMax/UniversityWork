import pandas as pd
from CombinatoireAlgorithms.Algorithm21 import GenerationOfNbitBinaryVectors


def TestAlg(end):
    end += 1
    operations = []
    n = range(1, end)
    for i in range(1, end):
        operations.append(GenerationOfNbitBinaryVectors(i))

    data = pd.DataFrame(
        {
            'n': n,
            'operations': operations
        }
    )
    print(data)