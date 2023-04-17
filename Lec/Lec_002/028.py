"""
Вывод значений через for:

"""
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))


print("")
print("********")

for (k,v) in dictionary.items(): # dictionary.items - это список [] где каждый элемент - кортеж!
    print(k, v)