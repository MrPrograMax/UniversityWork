from RegularSet import *

print("ТЕСТИРОВАНИЕ АЛГОРИТМА\n")

print("Три точки образующие правильный треугольник")
a = Point(0, 0)
b = Point(5, 5 * math.sqrt(3))
c = Point(10, 0)
array = [a, b, c]
print(f"Для множества {array}\nРегулярность = {IsRegularSet(array)}\n")

print("Точек меньше чем 3")
a = Point(0, 0)
b = Point(5, 5 * math.sqrt(3))
print(f"Для множества {array}\nРегулярность = {IsRegularSet(array)}\n")

print("ТЕСТИРОВАНИЕ РАБОТОСПОСОБНОСТИ\n")

print("Элемнеты принаделажат классу Point(x,y)")
arrray = [1, 3, 4]
print(f"Для множества {array}\nРегулярность = {IsRegularSet(array)}\n")
