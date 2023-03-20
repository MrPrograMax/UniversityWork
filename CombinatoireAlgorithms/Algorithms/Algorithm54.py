"""
1. Выделение компонент связности графа (Поиск в глубину)
2. Достижимость вершин орграфа         (Поиск в ширину)
3. Отыскание остовного дерева          (Поиск в ширину)
"""
#region Постановка решения задачи
"""
1. Задача выделения компонент связности графа. Эта задача мо-
жет быть решена с помощью поиска в глубину или ширину. Пусть поиск
начат с вершины s ∈ V. После его окончания, т. е. выделения компонен-
ты связности, содержащей вершину s, следует проверить, все ли вер-
шины графа отмечены. Если все вершины отмечены, то процесс обхода
завершить. Если нет, то обход возобновить с любой неотмеченной вер-
шины. Не представляет труда в алгоритме 5.1 предусмотреть вычисле-
ние числа k(G) компонент связности исходного графа G и вывод сооб-
щения о начале обхода вершин i-й компоненты, 1 ≤ i ≤ k(G).

2. Задача о достижимости вершин орграфа. Пусть заданы орг-
раф G = (V, E) и некоторая его вершина s ∈ V. Требуется найти множе-
ство всех вершин орграфа, достижимых из s. Говорят, что вершина v
достижима из вершины s, если в G существует путь, идущий от
вершины s к вершине v. Напомним, что путь – ориентированная
цепь.
Данная задача решается с помощью алгоритма 5.1. Для орграфа
обход вершины следует производить с учетом направленности дуг.
Направленность дуг полностью определяется списками смежности
орграфа. Обход надо начинать с вершины s. Все вершины, которые
удается отметить и пройти, достижимы из s.

3.Задача отыскания остовного леса. Пусть G = (V, E) – произ-
вольный граф, связный или несвязный. Всякий остовной ациклический
подграф T графа G называется его остовным (или стягивающим)
лесом. Очевидно, что остовной лес (n, m)-графа с k = k(G) компонен-
тами связности определяется через остовные деревья этих компонент
и, следовательно, содержит m = n – k ребер. Таким образом, задача
отыскания остовного леса сводится к выделению компонент связности
и нахождению для каждой из компонент остовного дерева. Все это
можно реализовать с помощью поиска в глубину или ширину
"""
# endregion

from queue import Queue, LifoQueue
from colorama import init, Fore
import numpy as np


class Graph:
    nodes = [] # Граф
    marked_points=[] # Текущие пройденые точки графа
    
    def __init__(self, friends, values=0):
        """
        friends - связи точки графа
        values - значение для этой точки
        """
        if values == 0:
            values = range(len(friends))
        elif len(friends) != len(values):
            raise Exception("Unequal sizes!")

        for i in range(len(friends)):
            self.nodes.append(Node(values[i], friends[i]))
        
        self.marked_poins = [0] * len(self.nodes)

    def search(self, index_point, key_word='width'):
        """
        index_point - начальная точка обхода
        key_word - метод обхода 'width' и 'depth
        возвращает массив с пройдеными точками
        """
        if key_word == 'width':
            queue = Queue()
        elif key_word == 'depth':
            queue = LifoQueue()
        else:
            raise Exception("Incorrect key word")

        result = []
        self.marked_poins = [0] * len(self.nodes)
        queue.put(index_point)

        self.marked_poins[index_point] = 1

        while queue.qsize() != 0:
            index = queue.get()
            result.append(index)
            for i in self.nodes[index].links:
                if self.marked_poins[i] == 0:
                    queue.put(i)
                    self.marked_poins[i] = 1

        return result

    def search_all(self, index_point, key_word='width'):
        """
        index_point - начальная точка
        key_word - Ключевое слово 'width' или 'depth', для обхода в ширину или глубину
        Возвращает массив с полным обходом графа
        """
        size = len(self.nodes)
        local_marked_points = [0]*size
        result = [0]*size
        
        first_search = self.search(index_point, 'width')
        #for i in result:

        #while local_marked_points != [1] * size:
            
            


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