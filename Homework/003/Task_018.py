# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
#     1 2 3 4 5
#     6
#     -> 5

print('')
number = int(input())
listNumber = []
searchNumber = 6
rezNumber = None
count = 1

for i in range(number):
    listNumber.append(count)
    count += 1

if searchNumber > len(listNumber):
    rezNumber = len(listNumber)
elif searchNumber == len(listNumber):
    rezNumber = len(listNumber) - 1
elif searchNumber == 1:
    rezNumber = 2
elif searchNumber < 1:
    rezNumber = 1
else:
    rezNumber = len(listNumber) + 1

print(*listNumber)
print(searchNumber)
print(f"-> {rezNumber}")
