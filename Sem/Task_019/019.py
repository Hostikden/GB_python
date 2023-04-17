# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

my_list = [1, 2, 3, 4, 5]
# print(my_list)

# k = 3

# my_list_right = my_list[:k+1]
# my_list_left = my_list[k+1:]

# rez_list = []

# for i in my_list_left:
#     rez_list.append(i)
# for i in my_list_right:
#     rez_list.append(i)

# print(rez_list)

# второй вариант:

# k = 2
# for i in range(k+1):
#     my_list.append(my_list.pop(0))
# print(my_list)

# третьий вариант:

k= 2 % len(my_list)
print(my_list[-k:] + my_list[:-k])
