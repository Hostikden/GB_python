def sum_numbers (n, y = "Hello"):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(sum_numbers(5))