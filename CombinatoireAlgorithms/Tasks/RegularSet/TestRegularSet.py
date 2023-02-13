from ResgularSet import *

print("ТЕСТИРОВАНИЕ АЛГОРИТМА\n")

print("Три точки образующие правильный треугольник")
a = Point(0, 0)
b = Point(5, 5 * math.sqrt(3))
c = Point(10, 0)
array = [a, b, c]
if IsRegularSet(array):
  print(f"Множество {array}\nРегулярно")
else:
  print(f"Множество {array}\nНерегулярно)
