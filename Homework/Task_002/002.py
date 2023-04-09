# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))

numberTree = number % 10
numberTwo = int(((number % 100)/10)//1)
numberOne = number//100

sumNumbers = numberOne + numberTwo + numberTree

print(sumNumbers)
