'''Схема мелиорации рисовых полей'''
from queue import Queue, LifoQueue


def is_ones(array) -> bool:
    '''Возвращает true, если все элементы равны единице
    '''
    for element in array:
        if element == 0:
            return False
    return True

def pos_zero(array) -> int:
    '''Возвращает позицию первого не нулевого элемента
       В случае, если такого не найдено, возвращает -1
    '''
    size = len(array)
    for i in range(size):
        if array[i] == 0:
            return i
    return -1

def get_links(array, size):
    '''Перевод из системы ребер в системы ссылок друзей у точек
    '''

    links = [ [] for x in range(size) ]

    for edge in array:
        if edge != []:
            links[edge[0]].append(edge[1])
            links[edge[1]].append(edge[0])

    for lin in links:
        lin.sort()

    return links

def cyclic_graph(array, key_word='width') -> bool:
    """ Проверка на то, что при добавлении нового ребра(new_edge)
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

    onedimension = [a for b in array for a in b]  # делаем его одномерным
    size = max(onedimension) + 1

    marked_points = [0 for x in range(size)]

    links = get_links(array, size)

    links_size = len(links)
    for i in range(links_size):
        if links[i] == []:
            marked_points[i] = 1

    parent = -1
    source = pos_zero(marked_points)

    marked_points[source] = 1
    queue.put((source, -1))

    while not queue.empty():
        (node2, parent) = queue.get()

        for node1 in links[node2]:
            if marked_points[node1] == 0:
                marked_points[node1] = 1
                queue.put((node1, node2))

            elif node1 != parent:
                return True

        if queue.empty() and not is_ones(marked_points):
            source = pos_zero(marked_points)
            if source != -1:
                queue.put((source, -1))

    return False

def search_ostav(points, weights):
    '''Возвращает пройденные подграфы через наименьший вес, без петлей
    '''
    if len(points) != len(weights):
        raise Exception("Unequal sizes!")

    # Синхронная сортировка ребер и их весов
    weights, points = zip(*sorted(zip(weights, points)))

    size = len(weights)
    edges = []

    for i in range(size):
        edges.append((points[i], weights[i]))

    ostav_result = [edges[0][0]]
    count_edge = 0

    for i in range(1, size-1):
        temp_arr = [edges[i][0]] + ostav_result

        # если с новым ребром не образуется цикл, то добавляем в результат
        if not cyclic_graph(temp_arr):
            ostav_result.append(edges[i][0])
            count_edge += 1

    return ostav_result, count_edge


rice_edges = {
    0: [0, 1],
    1: [0, 2],
    2: [0, 3],
    3: [1, 2],
    4: [1, 10],
    5: [2, 5],
    6: [2, 6],
    7: [2, 7],
    8: [3, 5],
    9: [3, 4],
    10: [4, 5],
    11: [4, 6],
    12: [5, 6],
    13: [6, 7],
    14: [6, 8],
    15: [7, 8],
    16: [7, 9],
    17: [7, 10],
    18: [8, 9],
    19: [9, 10]
}
rice_weights = {
    0 : 5,
    1 : 3,
    2 : 10,
    3 : 10,
    4 : 5,
    5 : 8,
    6 : 10,
    7 : 2,
    8 : 1,
    9 : 1,
    10: 1,
    11: 2,
    12: 10,
    13: 2,
    14: 1,
    15: 3,
    16: 1,
    17: 7,
    18: 1,
    19: 6
}

global_links = get_links(rice_edges.values(), 11)
result, count_edges = search_ostav(rice_edges.values(), rice_weights.values())

print(f'Ребра: {list(rice_edges.values())}')
print(f'Ссылки: {global_links}')
print(f'Результат: {result}\nКоличество ребер: {count_edges}')
