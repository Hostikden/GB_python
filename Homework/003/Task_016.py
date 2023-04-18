# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
#     1 2 3 4 5
#     3
#     -> 1

print('')
number = int(input())
searchNumber = 3
listNumber = []
count = 1

for i in range(number):
    listNumber.append(count)
    count += 1

print(*listNumber)
print(searchNumber)

# listNumber.append(3)                  раскомменируйте для проверки правильности подсчёта

count = 0
for i in range(0, len(listNumber)):
    if listNumber[i] == searchNumber:
        count += 1
    i += 1

print(f"-> {count}")

