def fib(n):
    a = 1
    b = 1
    for i in range(2,n):
        k = b 
        b = a + b
        a = k 
    return b 

def fib1(n):
    if n <= 1:
        return 1

    return fib1(n-1)+ fib1(n-2)


# print(fib(100))
print(fib1(100))