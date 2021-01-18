def trailingZeroes(n):
    value = factorial(n)
    count = 0
    i = 10
    while value % 10 == 0: 
        value = value // 10
        count += 1
    return count

def factorial(n):
    if n <= 1 : 
        return 1
    return (n * factorial(n-1))


print(trailingZeroes(20))
# print(factorial(20))