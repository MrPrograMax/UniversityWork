import itertools as iter
import numpy as np
import math

from CombinatoireAlgorithms.Algorithms.Algorithm31 import GenerationOfKElementSubsetsNElementSet


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = (x, y)

    def distance(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance

    def __str__(self):
        return f"({self.x}; {self.y})"


def IsRegularSet(set):

    if not IsValid(set):
        return 0

    dict = {}
    countOfPointsPair = len(GenerationOfKElementSubsetsNElementSet(len(set), 2))
    combinations = GenerationOfKElementSubsetsNElementSet(len(set), 3)
    for i in combinations:
        a = set[int(i[0])]
        b = set[int(i[1])]
        c = set[int(i[2])]
        if IsRightTriangle(a, b, c):
            dict[f'{np.array([i[0], i[1]])}'] = True
            dict[f'{np.array([i[0], i[2]])}'] = True
            dict[f'{np.array([i[1], i[2]])}'] = True
    return len(dict) == countOfPointsPair


def IsRightTriangle(a,b,c):
    dist1 = a.distance(b)
    dist2 = a.distance(c)
    dist3 = b.distance(c)
    return math.isclose(dist1, dist2) and math.isclose(dist1, dist3) and math.isclose(dist2, dist3)


a = Point(0, 0)
b = Point(5, 5 * math.sqrt(3))
c = Point(10, 0)
d = Point(10, 0)
A = [a, b, c]
print(IsRegularSet(A))

def IsValid(set):
    """
    set its list of class Point
    """
    if len(set) != 3:
        print(">> Ошибка! Код: 101: Размерность массива не равна 3")
        return False

    for i in range(len(set)):
        if not isinstance(set[i], Point):
            print(">> Ошибка! Код: 103: Элементы множества не являются объектами класса Point")
            return False