def largestPerimeter(A):
    if len(A) == 3:
        if(A[0] + A[1] > A[2] and A[0] + A[2] > A[1] and A[1] + A[2] > A[0]):
            return sum(A)
        else:
            return 0
    A = sorted(A, reverse=True)
    for i in range(0, len(A) - 2):
        first, second, third = A[i], A[i+1], A[i+2]
        if(first + second > third and first + third > second and second + third > first):
            return first + second + third
    return 0


print(largestPerimeter([3, 6, 2, 3]))
print(largestPerimeter([3, 3, 4, 2]))
