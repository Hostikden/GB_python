# Задача No1. Решение в группах
# За день машина проезжает n километров. 
# Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться 
# условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

import math
n = int(input("расстояние в день: "))
m = int(input("Всего км: "))

res = bool(m%n) + (m//n)
print(res)

# c = math.ceil(m/n)
# print(c)
# либо

s = (m+(n-1)) // n
print(s)