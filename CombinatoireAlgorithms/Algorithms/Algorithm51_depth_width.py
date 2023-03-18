import numpy as np

def width_graph_search(first_point, Links):
    """
        first_point - номер первой вершины графа, отчет с нуля
        Links - связи точек в графе по номерам 
    """
    ans_queue = [first_point]
    
    for point in ans_queue:
        for link in Links[point]:
            if link not in ans_queue:
                ans_queue.append(link)
    
    return ans_queue

def depth_graph_search(first_point, Links):
    """
        first_point - номер первой вершины графа, отчет с нуля
        Links - связи точек в графе по номерам 
    """
    ans_stack = [first_point]
    
    for point in ans_stack:
        reversed_array = Links[point].copy()
        reversed_array.reverse()

        for link in reversed_array:
            if link not in ans_stack:
                ans_stack.append(link)
    
    return ans_stack


Links = np.array([
    [0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
])

LN = [
    [1,2,4],
    [0,3,4],
    [0,4],
    [1,4],
    [0,1,2,3,4,5,6],
    [4,6],
    [4,5]
]
for i in range(len(LN)):
    print(i)
    print('Ширина = ',width_graph_search(i, LN))
    print('Долгота = ',depth_graph_search(i, LN))
