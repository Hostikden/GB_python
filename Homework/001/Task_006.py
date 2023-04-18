# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета
# 385916 -> yes
# 123456 -> no

tiket = int(input("Введите номер билета: "))

rightPart = tiket%1000
leftPart = int((tiket - rightPart)/1000)

numberOne = int((leftPart/100)%10)
numberTwo = int((leftPart/10)%10)
numberTree = leftPart%10

numberFour = int((rightPart/100)%10)
numberFive = int((rightPart/10)%10)
numberSix = rightPart%10

sumLeftPart = numberOne + numberTwo + numberTree
sumRightPart = numberFour + numberFive + numberSix

res = "Yes" if sumLeftPart == sumRightPart else "No"

print(res)