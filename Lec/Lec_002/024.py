'''
Пример добавления элемента в список

'''

list_1 = [1, 5]         # [1, 5]
print(list_1)

list_1.append(8)
print(list_1)           # [1, 5, 8]

'''
Пример добавления элементов в список с помощью цикла for

'''

list_2 = []
for i in range(5):
    list_2.append(i)
print(list_2)           # [0, 1, 2, 3, 4]