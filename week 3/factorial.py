def factorial1(n):
    while n > 0: 
        n = n // 10
        
def factorial(n):
    if n <= 1: 
        return 1
    return n * factorial(n -1)
factorial(1020)