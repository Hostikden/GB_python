# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('--> '))
s = 0
temp = 2
while temp < number:
    degreeTwo = pow(2, s)
    print(degreeTwo)
    s += 1
    temp += 2
