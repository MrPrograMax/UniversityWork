import numpy as np
from CombinatoireAlgorithms.TaskMilitaryBases import GetInfoAboutBastMilitaryBase

A = np.array([
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1]
])


losses = [0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1, 0.1]
GetInfoAboutBastMilitaryBase(9, A, losses)