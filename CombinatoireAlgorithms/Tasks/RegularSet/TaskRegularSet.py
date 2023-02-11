import itertools as iter
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
    countRigthtTriangles = 0
    needCount = len(list(iter.combinations(set, 2)))
    combinations = GenerationOfKElementSubsetsNElementSet(len(set), 3)
    for i in combinations:
        a = set[int(i[0])]
        b = set[int(i[1])]
        c = set[int(i[2])]
        if IsRightTriangle(a, b, c):
            countRigthtTriangles += 3

    return needCount == countRigthtTriangles


def IsRightTriangle(a,b,c):
    dist1 = a.distance(b)
    dist2 = a.distance(c)
    dist3 = b.distance(c)
    return math.isclose(dist1, dist2) and math.isclose(dist1, dist3) and math.isclose(dist2, dist3)


a = Point(0, 0)
b = Point(5, 5 * math.sqrt(3))
c = Point(10, 0)
d = Point(10, 0)
A = [a, b, c, d]
print(IsRegularSet(A))
