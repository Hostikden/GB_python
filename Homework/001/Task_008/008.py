# Задача 8: Требуется определить, можно ли от 
# шоколадки размером n ×mk долек отломить
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).
# 3 2 4 -> yes 
# 3 2 1 -> no

height = int(input("Введите длину шоколадки: "))
width = int(input("Введите ширину шоколадки: "))
segment = int(input("Введите размер желаемой дольки: "))

if segment == height or segment == width:
    print("Yes")
if segment < height and segment < width:
    print("No")
if segment > height*width:
    print("No")
if segment%width == 0 or segment%height == 0:
    print("Yes")