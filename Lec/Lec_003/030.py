# Задание: Необходимо создать функцию sumNumbers(n), которая будет считатьсумму всех элементов от 1 до n.

def sum_numbers (n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(sum_numbers(5))