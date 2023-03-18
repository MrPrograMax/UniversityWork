from queue import Queue, LifoQueue
from colorama import init, Fore
import numpy as np


class Graph:
    nodes = []

    def __init__(self, friends, values=0):
        if values == 0:
            values = range(len(friends))
        elif len(friends) != len(values):
            raise Exception("Unequal sizes!")

        for i in range(len(friends)):
            self.nodes.append(Node(values[i], friends[i]))

    def search(self, index_point, key_word='width'):
        if key_word == 'width':
            queue = Queue()
        elif key_word == 'depth':
            queue = LifoQueue()
        else:
            raise Exception("Incorrect key word")

        result = []
        x = [0] * len(self.nodes)
        queue.put(index_point)

        x[index_point] = 1

        while queue.qsize() != 0:
            index = queue.get()
            result.append(index)
            for i in self.nodes[index].links:
                if x[i] == 0:
                    queue.put(i)
                    x[i] = 1

        return result


class Node:
    def __init__(self, value, links):
        self.value = value
        self.links = links


LN = [
    [1, 2, 4],
    [0, 3, 4],
    [0, 4],
    [1, 4],
    [0, 1, 2, 3, 4, 5, 6],
    [4, 6],
    [4, 5]
]

graph = Graph(LN)
init(autoreset=True)
for i in range(len(LN)):
    print(Fore.GREEN + f"Начальная точка: {i}")
    print(f"В ширину: {graph.search(i, 'width')}")
    print(f"В глубину: {graph.search(i, 'depth')}\n")
