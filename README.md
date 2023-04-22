# Литература:

Книги для изучения. Рекомедую читать именно в таком порядке:

- Byte of Python, Swaroop C. H.
- Грокаем алгоритмы, Адитья Бхаргава
- Изучаем Python (1, 2 том), Марк Лутц
- IDE, которую использовал на семинаре: https://www.onlinegdb.com/online_python_compiler
- PyCharm: https://www.jetbrains.com/ru-ru/pycharm/
- Дзен Python: https://tyapk.ru/blog/post/the-zen-of-python

## Лекция I:

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

### Множественное присваивание в Python:

    a, b = 1, 3
    a = b = 4

### Как узнать тип данных переменной:

- print(type(test))

### Как вставить в строку кавычку:

    test = 'example \'example\''
    test = 'example "example"'
    
    В пределах тройных кавычек можно выводить отдельными строками.
    print('''1              # 1
    2                       # 2
    3 ''')                  # 3

    Строку можно умножать
    print('la'*5)           # lalalalala

### Комментирвоание строк:

- #test
- """ test """

### Некотрые функции:

**abs()** - находит модуль числа и принимает на вход одно значение. Модуль числа - это абсолютная величина, то есть, грубо говоря, модуль числа отбрасывает знак.

**min()** - принимает на вход несколько значений через запятую и находит самое наименьшее из них. 

**max()** - принимает на вход несколько значений через запятую и находит самое наибольшее из них. 

**pow()** - принимает на вход 2 значения и возводит первое число в степень второго.

**round()** - принимает на вход значение и выполняет округление по умолчанию до целого числа. Также, если через запятую указать разряд, то функция будет округлять до какого значения после точки нужно округлять.
Также в round() можно передать неявные значения. Например, если передать ей вторым значением -1, то она округлит ее до первого знака до запятой:

    print(round (456, -1)) # 460

В Python есть функция **type()**, которая принимает объект и возвращает тип данного объекта:

### Ввод нескольких переменных:
    Но при помощи int(input()) вы можете считать только одно число в одной строке. Если вам потребуется ввести несколько чисел в одну строчку через пробел, нужно поступать следующим образом:

    a, b = input().split() # вводится ТОЛЬКО 2 числа через пробел
    a = int(a)
    b = int(b)
    print(a, b)
    print(type(a),type(b))

    Здесь вводятся только два значения в одну строку через пробел. Затем каждое из них преобразуется к целому значению.

    Другой способ прочитать несколько значений - использовать функцию map

    a, b, c = map(int, input().split()) #считываем 3 целых числа через пробел
    print(a,b,c)

    Варианты использования функцииinput()

    a = input() - если необходимо ввести строку и сохранить ее в переменную а
    a = int(input()) - если необходимо ввести целое число и сохранить его в переменную а
    a = float(input()) - если необходимо ввести вещественное число и сохранить его в переменную а
    a,b = map(int,input().split()) - если необходимо ввести два целых числа в одну строку через пробел
    a,b,c = map(float,input().split()) - если необходимо ввести три вещественных числа в одну строку через пробел

### Замена переменных местами:

    a, b = b, a

    Математический вариант:

    a = a + b
    b = a - b
    a = a - b

### Ввод данных:

- input()
- test = input() - записываем в переменную, но для лучшего вида можем указать сверху пришлащение для ввода через print:
- - print("Введите данные: ")
- - test = input()

альтернативный вариант для ввода в одну строку:

- test = input('Веведите второе число: ') - сообщение нигде не сохраняется, только введённое значение

### print(value, ..., sep=' ', end='\n')

    print(1, 2, 3, 4)                   # 1 2 3 4
    print(1, 2, 3, 4, sep=' ')          # 1 2 3 4
    print(1, 2, 3, 4, sep='')           # 1234
    print(1, 2, 3, 4, sep=',')          # 1,2,3,4
    print(1, 2, 3, 4, sep='*')          # 1*2*3*4
    print(1, 2, 3, 4, sep='###')        # 1###2###3###4

    print(1, 2, 3, end='!')             # не будет переноса в конце
    print('hello', end='\n')            # здесь будет перенос
    print(5, 6, 7)                      # и здесь будет перенос

### Range

    a = input()
    print(*range(1,6), sep= a)

### Деление

В python данная операция обозначается знаком двойного слеша //. И допустим если вам надо нацело поделить a на b (a//b), 
нужно ответить на вопрос: «Cколько раз второе число (в нашем случае b) умещается в первое?»

Остаток от деления в python обозначается знаком процента %. Чтобы посчитать, вы должны ответить на вопрос:
«Сколько останется от первого числа после того, как в него максимальное количество раз уместится второе число?»

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

Однако, в ООП использование функции break не является правилом хорошего тона и на замену приходит вариант с флагом:

    пример: Lec/Lec_001/003.py

### Цикл for, функция range()

В python цикл for в основном используется для перебора значений
Пример использовния цикла for:

    for i in enumeration:
        # operator 1
            # operator 2
            # ...
            # opearator n
    
    for i in 1, -2, 3, 14, 5:
        print(i)

    # 1 -2 3 15 5

пример: Lec/Lec_001/004.py

- Range выдает значения из диапазона с шагом 1.
- Если указано только одно число - от 0 до заданного числа не включая его.
- Если нужен другой шаг, третьим аргументом модно задать приращение.

    r = range(5) # 0 1 2 3 4 5
    r = range(2, 5) # 2 3 4
    r = range(0, -5) # ---- ошибка, тк дефолтное ранво + 1
    r = range(1, 10, 2) # 1 3 5 7 9
    r = rnge(100, 0, -20) # 100 80 60 40 20

пример: Lec/Lec_001/005.py

Так же цикл for можно использовать со строками, так как у строк есть нумерация, такая же как у массивов, начинается с 0:

    for i in 'qwerty':
        print(i)
    # q
    # w
    # e
    # r
    # t
    # y

пример: Lec/Lec_001/006.py

Значит мы можем вывести букву в строке по её индексу:
    a = 'qwerty'
    print(a[0])

Пример вложенного цикла:

Lec/Lec_001/007.py

### Строки:

    len - помогает узнать размер нашей строки
    print('ещё' in text) - помогает узнать есть ли слово "ещё" в нашей строке, выводит булево значение
    lower - позволяет преобразовать строку в нижний регистр
    upper - преоброзовывает в верхний регистр
    replace - изменение символов, принимает два аргумента (какое изменяем и на какое изменяем)

пример: Lec/Lec_001/008.py

### Срезы в строках:

пример: Lec/Lec_001/008.py

## Лекция II:

### Списки:

Список - это упорядоченный конечный набор элементов. Это тот же самый массив, в котором можно хранить элементы любых типов данных. Нумерация элементов списка начинается с нуля.

    list_1 = []         # создание пустого списка
    list_2 = list()     # создание пустого списка
    
    list_1 = [1, 9, 11, 13, 15, 17]
    print(list_1[0])    # Ответ:  7

если мы не хотим вывод с **квадратными скобками**, то нам необходимо поставить *:
    
    print(*list_1)

пример: Lec/Lec_002/021.py

В списке мы можем работать с циклом for:

    for i in list_1:
        print(i)

пример: Lec/Lec_002/022.py

Вывод размера(длины) списка:

    len(list_1)

Обращение к элементу списка:

    list_1[0]

пример: Lec/Lec_002/023.py

Добавление элементов в список:

    list_1.append(8)

пример: Lec/Lec_002/024.py
 
### Функции списков:

Удаление последнего элемента функцией pop.

    list_1 = [12, 7, -1, 21, 0]

    print(list_1)                   # [12, 7, -1, 21]
    print(list_1.pop())             # 21
    print(list_1)                   # [12, 7, -1]
    print(list_1.pop())             # -1
    print(list_1)                   # [12, 7] 

Важно, что pop возвращает значение! То есть введя переменную a - мы можем вывести значение последнего элемента:

    list_1 = [12, 7, -1, 21, 0]
    a = list_1.pop()                # 0

Удаление конкретного элемента:

    list_1 = [12, 7, -1, 21, 0]
    print(list_1.pop(0))            # 12
    print(list_1)                   # [7, -1, 21, 0]

Добавление элемента на нужную позицию:

    list_1 = [12, 7, -1, 21, 0]
    print(list_1.insert(2, -11))            # два аргумента: позиция и значение
    print(list_1)                   # [12, 7, 11, -1, 21, 0]

Срезы в списках:

    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_1[0])                            # 1
    print(list_1[0])                            # 2
    print(list_1[len(list_1)-1])                # 10
    print(list_1[-5])                           # 6
    print(list_1[:])                            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_1[:2])                           # [1, 2]
    print(list_1[len(list_1)-2:])               # [9, 10]
    print(list_1[2:9])                          # [3, 4, 5, 6, 7, 8, 9]
    print(list_1[6:-18])                        # []
    
    print(list_1[0:len(list_1):6])              # [1, 7]
    print(list_1[::6])                          # [1, 7]

### Кортеж:

Кортеж - неизменяемый список.
Кортеж занимает меньше места в памяти и работает быстрее, по сравнению со списками.
Используют для защиты данных от изменений.

    t = ()              # создание пустого кортежа
    print(type(t))      # class <'tuple'>

    t = (1)             # без запятой в конце
    print(type(t))      # class <'int'> 

    t = (1,)            # с запятой в конце    
    print(type(t))      # class <'tuple'> 

Преобразование списка в кортеж:

    v = [1, 5, 8]            # создаем список
    v = tuple(v)             # преобразовываем в кортеж

Преобразование кортежа в отдельные элементы:

    v = (1, 5, 8)
    a, b, c = v
    print(a, b, c)            # [1, 5, 8]

Вывод кортежа через for:

    t = (1, 2, 3, 5,)
    for i in t:
        print(i)

    либо

    for i in range(len(t)):
        print(t[i])

Минус кортежа:

    Нельзя вывести 'итый' элемент, то есть

    t = (1, 2, 3, 5,)
    t[0] = 2                # НЕ СРАБОТАЕТ

    А в списках такая запись сработала бы!

### Словари:

Словари - неупорядочненные коллекции проивольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. В словаре для определения элемента используется значение ключа (строка, число).

Создание пустого словаря:

    d = {}
    d = dict()
    пример: Lec/Lec_002/025.py

    # создали словарь
    dictionary = {}
    # внесли значения в словарь
    dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
    print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
    print(dictionary['left']) # ←

Добваление нового ключа в словарь:

    dictionary[895] = 98998
    пример: Lec/Lec_002/026.py

Удаление элемента в словаре:

      del dictionary['left'] # удаление элемента
      пример: Lec/Lec_002/027.py

Типы ключей могут отличаться, можно использовать даже словарь в словаре!

    print(dictionary['up']) # ↑
    dictionary['left'] = '⇐'
    print(dictionary['left']) # ⇐

если мы обратимся к несуществующему ключу - будет ошибка:

    print(dictionary['type']) # KeyError: 'type'

Вывод значений через for:

    for item in dictionary:                              
    print('{}: {}'.format(item, dictionary[item]))
    
    # up: ↑
    # down: ↓
    # right: →

    Либо:

    for (k,v) in dictionary.items(): # dictionary.items - это список [] где каждый элемент - кортеж!
        print(k, v)

    # up ↑
    # down ↓
    # right →

    пример: Lec/Lec_002/028.py

### Множества:

Множества содержат в себе уникальные элементы, не обязательно
упорядоченные.

Одно множество может содержать значения любых типов. Если у Вас есть два
множества, Вы можете совершать над ними любые стандартные операции,
например, объединение, пересечение и разность. Давайте разберем их.

    colors = {'red', 'green', 'blue'}
    print(colors) # {'red', 'green', 'blue'}
    colors.add('red')
    print(colors) # {'red', 'green', 'blue'}
    colors.add('gray')
    print(colors) # {'red', 'green', 'blue','gray'}
    colors.remove('red')
    print(colors) # {'green', 'blue','gray'}
    colors.remove('red') # KeyError: 'red'
    colors.discard('red') # ok аналог remove только с проверкой на наличие такого же элемента во множестве, если такой элемент отсутвует, то discard пропкскает строку и не выдает ошибку
    print(colors) # {'green', 'blue','gray'}
    colors.clear() # { } удалить все элементы
    print(colors) # set()

Операции со множествами в Python

    a = {1, 2, 3, 5, 8}
    b = {2, 5, 8, 13, 21}
    c = a.copy() # c = {1, 2, 3, 5, 8}                              # копия
    u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}                    # объединение
    i = a.intersection(b) # i = {8, 2, 5}                           # пересечение == &
    dl = a.difference(b) # dl = {1, 3}                              # разность a от b
    dr = b.difference(a) # dr = {13, 21}                            # разность b от a
    q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}     # функция пересечение a и b, потом a объеденяем с b, затем находим разность с полученным мнодеством пересечения!

**Неизменяемое или замороженное множество(frozenset)** — множество, с которым
не будут работать методы удаления и добавления.

    a = {1, 2, 3, 5, 8}
    b = frozenset(a)    # теперь мы никак не можем его изменить
    print(b) # frozenset({1, 2, 3, 5, 8})

![Alt-текст](https://raw.githubusercontent.com/Hostikden/GB_python/main/src/img/1.webp)

### List Comprehension

У каждого языка программирования есть свои особенности и преимущества. Одна из
культовых фишек Python — list comprehension (редко переводится на русский, но можно
использовать определение «генератора списка»). Comprehension легко читать, и их
используют как начинающие, так и опытные разработчики. List comprehension — это
упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
if-else для определения того, что в итоге окажется в финальном списке.

    Простая ситуация — список:
        list_1 = [exp for item in iterable]
    
    Выборка по заданному условию:
        list_1 = [exp for item in iterable (if conditional)]

    Задача 1
        Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
    Решение:
        Создать список чисел от 1 до 100
        list_1 = []
        for i in range(1, 101):
        list_1.append(i)
        print(list_1) # [1, 2, 3,..., 100]
        Эту же функцию можно записать так:
        list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

    Задача 2
        Добавить условие (только чётные числа)
        list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
        Допустим, вы решили создать пары каждому из чисел (кортежи)
        list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
        Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
        list_1 = [i * 2 for i in range(10) if i % 2 == 0]
        print(list_1) # [0, 4, 8, 12, 16]

### Профилирование и отладка

    ● **IndentationError (Ошибка отступов)**
    number_first = 5
    number_second = 7
    if number_first > number_second:
    print(number_first) # !!!!!

    ● **TypeError (Типовая ошибка)**
    text = 'Python'
    number = 5
    print(text + number)
    # Нельзя складывать строки и числа

    ● **ZeroDivisionError(Деление на 0)**
    number_first = 5
    number_second = 0
    print(number_first // number_second)
    # Делить на 0 нельзя

    ● **KeyError(Ошибка ключа)**
    dictionary = {1: 'Monday', 2: 'Tuesday'}
    print(dictionary[3])
    # Такого ключа не существует

    ● **NameError(Ошибка имени переменной)**
    name = 'Ivan'
    print(names)
    # Переменной names не существует

    ● **ValueError(Ошибка значения)**
    text = 'Python'
    print(int(text))
    # Нельзя символы перевести в целые значения

### Способ остановки цикла While:

    num  = 23
    run = True

    while run:
        guess = int(input("Введите целое число: "))

        if guess == num:
            print("Вы йгадали число!")
            run = False
        elif guess < num:
            print("Загаданное число больше этого")
        else:
            print("Загаданное число меньше этого")
    else:
        print("Цикл while закончен")

    
### Функция и рекурсия

**Функция** — это фрагмент программы, используемый многократно:

**Alias** (псевдоним) — альтернативное имя, которое даётся функции при её импорте
из файла.

**Рекурсия** — это функция, вызывающая сама себя.

Пример функции: Lec/Lec_003/030.py

    def sum_numbers (n):
        sum = 0
        for i in range(1, n + 1):
            sum += i
        return sum

Очень важно понимать одну вещь, сколько аргументов мы передаем, столько и принимаем. Или наоборот сколько аргументов мы принимаем, столько и передаем. В нашем случае функция sumNumbers принимает 1 аргумент(n).

Однако, мы можем создать дефолтное значение второго аргумента.

Пример такого решения: Lec/Lec_003/031.py

        def sum_numbers (n, y = "Hello"):
            print(y)
            sum = 0
            for i in range(1, n + 1):
                sum += i
            return sum

И теперь, когда мы захотим передать своё значение во второй аргумент (y), то наше дефолтное значение (Hello) заменится.

Если мы не знаем какое воличество аргументов хотим передать, то мы ставим *

Пример такого решения: Lec/Lec_003/032.py

     В Python можно перемножать строку на число

     def new_string(symbol, count=3):
        return symbol * count
    print(new_string('!', 5)) # !!!!!
    print(new_string('!')) # !!!
    print(new_string(4)) # 12


### Модульность

    import modul1                   # импорт модуля, но при таком варианте при вызове функции нам будет необходимо обращаться через (например, mudul1.max1)
    
    import modul1 as m1             # импорт модуля как имя m1 и теперь при вызове функции нам будет необходимо обращаться через (например, m1.max1)

    from modul1 import max1         # импорт конкретной функции 

    from modul1 *                   # импорт всех функций модуля

### Рекурсия

При описании рекурсии важно указать, когда функции надо остановиться и перестать вызывать саму себя. По-другому говоря, необходимо указать базис рекурсии
