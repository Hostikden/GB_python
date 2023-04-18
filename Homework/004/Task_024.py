# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки
# Пример:
# 4 -> 1 2 3 4
# 9

control_module = [1, 2, 3, 4]
dictionary = {}
max_collect_module = -1

count = 1
for i in control_module:
    if i == control_module[0]:
        dictionary[count-1] = control_module[0] + control_module[-1] + control_module[1]
    elif i == control_module[-1]:
        dictionary[count-1] = control_module[0] + control_module[-1] + control_module[-2]
    else:
        dictionary[count-1] = control_module[count - 2] + control_module[count - 1] + control_module[count]
    count += 1

for (k,v) in dictionary.items():
    if v > max_collect_module:
        max_collect_module = v

print(f"{len(control_module)} -> {control_module}")
print(max_collect_module)