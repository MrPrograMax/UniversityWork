""" Импорт структуры очередь и стек(лифо) """
from queue import Queue, LifoQueue


class Node:
    """Узел, содержит значение и ссылки"""
    def __init__(self, value, links):
        self.value = value
        self.links = links


class Edge:
    """Ребро, содержит образующие точки, и свой вес"""
    def __init__(self, points, weight):
        self.edge = [points[0], points[1]]
        self.weight = weight


class Graph:
    """Граф, инициализируется через Node"""
    
    nodes = []  # Граф
    marked_points = []  # Текущие пройденые точки графа

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

        self.marked_points = [0] * len(self.nodes)

    def search(self, index_point=0, key_word='width'):
        """
        index_point - начальная точка обхода
        key_word - метод обхода 'width' и 'depth'
        возвращает массив с пройдеными точками
        """
        if key_word == 'width':
            queue = Queue()
        elif key_word == 'depth':
            queue = LifoQueue()
        else:
            raise Exception("Incorrect key word")

        self.marked_points = [0] * len(self.nodes)
        result = []
        queue.put(index_point)

        self.marked_points[index_point] = 1

        while queue.qsize() != 0:
            index = queue.get()
            result.append(index)
            for i in self.nodes[index].links:
                if self.marked_points[i] == 0:
                    queue.put(i)
                    self.marked_points[i] = 1

        return result

    def search_all(self, index_point=0, key_word='width'):
        """
        index_point - начальная точка
        key_word - Ключевое слово 'width' или 'depth', для обхода в ширину или глубину
        Возвращает:
            1. массив с полным обходом графа
            2. Колличество найденых подграфов
        """
        size = len(self.nodes)
        local_marked_points = [0]*size  # Пройденные точки в этой функции
        result_all = []
        count_of_subgraphs = 1  # Колличество найденых подграфов

        # Начинаем с первого обхода
        temp_search = self.search(index_point, key_word)

        # Заполняем результирующий массив первым обходом
        result_all += temp_search

        # Заполняем пройденные точки первого обхода
        for i in range(size):
            local_marked_points[i] += self.marked_points[i]

        # Пока не будут пройдены все точки графа, цикл будет запускать поиск по порядку
        for i in range(size):
            if local_marked_points[i] == 0:
                temp_search = self.search(i, key_word)
                # Присоединение к результирующему списку новый подграф
                result_all += temp_search
                # Добавление точек в уже пройденные
                for i in range(size):
                    local_marked_points[i] += self.marked_points[i]

                count_of_subgraphs += 1

        return result_all, count_of_subgraphs

    def search_split(self, key_word='width'):
        """
        key_word - метод обхода
        Возвращает список со списками обходов всех подграфов
        """
        result_split = []
        size = len(self.nodes)
        local_marked_points = [0]*size  # Пройденные точки в этой функции
        count_of_subgraphs = 1  # Колличество найденых подграфов

        # Начинаем с первого обхода
        temp_search = self.search()  # По уумолчанию index=0, key_word='width

        # Заполняем результирующий массив первым обходом
        result_split.append(temp_search)

        # Заполняем пройденные точки первого обхода
        for i in range(size):
            local_marked_points[i] += self.marked_points[i]

        # Пока не будут пройдены все точки графа, цикл будет запускать поиск по порядку
        for i in range(size):
            if local_marked_points[i] == 0:
                temp_search = self.search(i, key_word)
                # Добваление в результирующий спискок новый подграф
                result_split.append(temp_search)
                # Добавление точек в уже пройденные
                for i in range(size):
                    local_marked_points[i] += self.marked_points[i]

                count_of_subgraphs += 1

        return result_split, count_of_subgraphs

    def get_links(self, array, size):
        """Перевод из системы ребер в системы ссылок друзей у точек"""
       
        links = [ [] for x in range(size) ]
        
        for edge in array:
            #print(edge)
            if edge != []:
                links[edge[0]].append(edge[1])
                links[edge[1]].append(edge[0])
                
        for lin in links:
            lin.sort()

        return links

    def cyclic_graph(self, array, index_point=0, marked_points = None, parent=-1, key_word='width'):
        """
            Проверка на то, что при добавлении нового ребра(new_edge)
            Не будет создаваться цикл с текущами ребрами из queue
            Если известны связи все точки ребер edges
            Если он создатся, вернуть True
        """
        if key_word == 'width':
            queue = Queue()
        elif key_word == 'depth':
            queue = LifoQueue()
        else:
            raise Exception("Incorrect key word")
        print(f'array={array}')

        onedimension = [a for b in array for a in b] #делаем его одномерным    
        print(onedimension)
        size = max(onedimension) + 1
        print(size)
        links = self.get_links(self, array, size)

        if not marked_points:
            marked_points = [0 for x in range(size)]

        marked_points[index_point] = 1

        for w in links[index_point]:
            if not marked_points[w]:
                if self.cyclic_graph(self, array, w, marked_points, index_point):
                    return True
            elif w!= parent:
                return True
        """
        for index_point in range(len(links)):
            if links[index_point] == []:
                pass
            else:
                queue.put(index_point)
                marked_points[index_point] = 1
                break

        print(f'links={links}')
        while queue.qsize() != 0:
            index = queue.get()

            flag = True

            #кринж это вообще не работает он прыгает между двумя точками бесконечно
            #сразу останавливаясь на марках

            for i in links[index]:
                print(f'\ni={i}, index={index}\nMark={marked_points}')
                
                #попытка проверки на то что он ссылается на одно ребро, пока безуспешно
                if [i,index] in array or [index, i] in array:
                    flag = False
                    pass

                if marked_points[i] == 0:
                    queue.put(i)
                    marked_points[i] = 1
                else:
                    return True
            if links[index] == []:
                queue.put(index+1)
        """
        return False
        
    def search_ostav(self, points, weights):
        """Возвращает пройденные подграфы через наименьший вес, без петлей"""        
        if len(points) != len(weights):
            raise Exception("Unequal sizes!")       
        
        #Синхронная сортировка ребер и их весов
        weights, points = zip(*sorted(zip(weights, points)))

        size = len(weights)
        edges = []
    
        for i in range(size):
            #edges.append(Edge(points[i], weights[i]))
            edges.append((points[i], weights[i]))
        
        print(edges)
        print()

        #ostav_result = [edges[0].weight]
        ostav_result = [edges[0][0]]
        count_edge = 0
        
        for i in range(1, size-1):
            #if not cyclic_graph(edges[i].edge, ostav_result):
            
            print(f'im {i} edge {edges[i][0]}')
            
            print(f'All edges {ostav_result + [edges[i][0]]}')
            temp_arr = [edges[i][0]] + ostav_result
            print(f'temp = {temp_arr}')
            #если с новым ребром не образуется цикл, то добавляем в результат
            if not self.cyclic_graph(self, temp_arr):
                ostav_result.append(edges[i][0])
                count_edge += 1

            print(ostav_result)
            print()

        return ostav_result, count_edge

    def print_all_info(self, index_point=0, key_word='width'):
        print(f'Пройденный граф(search) = {self.search(index_point, key_word)}')

        result, count = self.search_all(index_point, key_word)
        print(f'Пройденный полностью граф(search_all) = {result}')

        result, count = self.search_split(key_word)
        print(f'Пройденные полностью подграфы(search_split) = {result}')
        print(f'Колличество графов = {count}\n')

# region useless stuff
LN = [
    [1, 2, 4],
    [0, 3, 4],
    [0, 4],
    [1, 4],
    [0, 1, 2, 3, 4, 5, 6],
    [4, 6],
    [4, 5]
]

orgraf_snake = [
    [1, 2],
    [3, 4],
    [4],
    [5],
    [5],
    []
]

double_graph = [
    [1],
    [0],
    [3, 4],
    [2, 4],
    [3, 2]
]

# graph = Graph(LN)
# graph.print_all_info()

#dgraph = Graph(double_graph)
#dgraph.print_all_info()

# orgraph = Graph(orgraf_snake)
# orgraph.print_all_info()

ostav_graph = [
    [1, 5, 4],
    [0, 2, 4],
    [1, 3],
    [2, 4, 5],
    [0, 1, 3, 5],
    [0, 3, 4]
]

ostav_weight = [
    [10, 8, 9],
    [10, 2, 6],
    [2, 5],
    [5, 4, 6],
    [9, 6, 4, 1],
    [8, 3, 1]
]
#endregion

#Точки соединений ребер
ost_edges = [
    [0, 1],
    [0, 5],
    [1, 2],
    [1, 4],
    [2, 3],
    [3, 4],
    [3, 5],
    [4, 0],
    [4, 5]
]
# Веса соответствующих ребер
ost_edges_weights = [
    10,
    8,
    2,
    6,
    5,
    4,
    3,
    9,
    1
]

print(Graph.get_links(Graph, ost_edges, 6))
print('\n')
print(Graph.search_ostav(Graph, ost_edges, ost_edges_weights))
