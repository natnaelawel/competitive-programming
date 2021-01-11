def numIdenticalPairs(nums):
    resultList = dict()
    for i in range(len(nums)):
        if resultList.get(nums[i]):
            resultList[nums[i]] += 1
        else:
            resultList[nums[i]] = 1
    count = 0
    for k, v in resultList.items():
        if v > 1:
            print(k, v)            
            count += (factorial(v) // (2 * factorial(v-2)))
            print(count)

    return count
def factorial(n): 
    product = 1
    while n > 1:
        product *= n 
        n -= 1
    return product

nums = [1, 2, 3, 1, 1, 3]
nums = [1, 1, 1, 1]
nums = [1, 2, 3, 4]
print(numIdenticalPairs(nums))
