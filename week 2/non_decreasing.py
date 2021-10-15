import math


def checkPossibility(nums):
    isChanged = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            if isChanged:
                return False
            if i != 0 and nums[i-1] > nums[i+1]:
                nums[i + 1] = nums[i]
            isChanged = True

    return True
   

nums = [4, 2, 1]
nums = [4,2,3]

# nums = [3, 4, 2, 3]
nums = [0, 0, 0, 0]
# nums = [-1,4,2,3]
# nums = [1,1,1,1]
# nums = [5, 7, 1, 8]
print(checkPossibility(nums))
