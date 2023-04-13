# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import math

numberOne = 168
numberTwo = 10

numberS = numberOne + numberTwo
numberP = numberOne*numberTwo

if numberOne > 1000 or numberTwo > 1000:
    print('Введено неверное число')
else:
    x = (numberS - math.sqrt(numberS**2-4*numberP))/2
    y = numberS - x
    print(f'Если сумма чисел = {numberS}, а произведение = {numberP},')
    print(f'то первое число = {int(x)}, а второе = {int(y)}')
