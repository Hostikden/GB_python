# Литература:

Книги для изучения. Рекомедую читать именно в таком порядке:

- Byte of Python, Swaroop C. H.
- Грокаем алгоритмы, Адитья Бхаргава
- Изучаем Python (1, 2 том), Марк Лутц
- IDE, которую использовал на семинаре: https://www.onlinegdb.com/online_python_compiler
- PyCharm: https://www.jetbrains.com/ru-ru/pycharm/
- Дзен Python: https://tyapk.ru/blog/post/the-zen-of-python

## I семинар:

### Создаём виртуальное окружение:

- python3 -m venv .folder 

### Вывод данных:

- print (a, b, c)
- print (a, ' - ', b, ' - ', c)

### Интерполяция :

- print(f"{a} - {b} - {c}")
- print("{} - {} - {}".format(a, b, c))

### Типы данных:

- int - целые числа
- float - дробные числа
- bool - логический тип данных
- str - строка

### Пустое значение для переменной:

- test = None

### Строковое значение для переменной:

- test = "example"
- test = 'example'

### Как узнать тип данных переменной:

- print(type(test))

### Как вставить в строку кавычку:

- test = 'example \'example\''

- test = 'example "example"'

### Комментирвоание строк:

- #test
- """ test """

### Ввод данных:

- input()
- test = input() - записываем в переменную, но для лучшего вида можем указать сверху пришлащение для ввода через print:
- - print("Введите данные: ")
- - test = input()

альтернативный вариант для ввода в одну строку:

- test = input('Веведите второе число: ') - сообщение нигде не сохраняется, только введённое значение

### Явное указание типа данных:

- test = str(c)
- test = int(input())

### Арифметические операции:

- ' + ' - сложение
- ' - ' - вычитание
- ' * ' - умножение
- ' / ' - деление
- ' % ' - остаток от деления
- ' // ' - целочисленное деление
- ' ** ' - возведение в степень

### Округление:

- round(n, 2) - два аргумента (число и количество знаков после запятой)

### Логические операции:

- ' = ' - равно
- ' > ' - больше
- ' < ' - меньше
- ' >= ' - больше либо равно
- ' <= ' - меньше либо равно
- ' == ' - проверяет равны ли значения
- ' != ' - проверяет на неравеноство
- ' not ' - не (отрицание) 
- ' and ' - и (коньюнкция)
- ' or ' - или (дизьюнкция)

### if-else:

    if condotion:
        # operation 1
        # operation 2
        # ...
        # operation n
    else:
        # operation n + 1
        # operation n + 2
        # ...
        # operation n + m

### else-if -> в связке с elif

    if condition1:
        # operator
    elif condition2:
        # operator
    elif condition3:
        # operator
    else:
        # operator

### Сложные условия and, or, not:

    if condition1 and condition2: (выполнится, когда оба условия окажутся верными)
    #operator
    if condition 3 or condition4: (выполнится, когда хотя бы одно из условий окажется верным)
    # operator

### Цикл while:

    while condition:
        # operator 1
        # operator 2
            # ...
            # operator n

### Цикл while-else:

Блок else выполняется только в том случае, когда основное тело цикла перестает работать **самостоятельно** . Этому может помешать, например, **break**.

    while condition:
        # operation 1
        # operation 2
            # ...
            # operation n
    else:
        # operatoin n + 1
        # operatoin n + 2
        # ...
        # operatoin n + m

