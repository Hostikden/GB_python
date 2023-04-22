# def fib (n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
    
#     return fib (n-1) + fib (n-2)

def fib (n):
    if n in range(0,2):
        return 1
    return fib (n-1) + fib (n-2)

print(fib(7))