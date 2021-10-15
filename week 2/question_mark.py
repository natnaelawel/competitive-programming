def solution(nums):
    if nums = None or nums.index("?") == -1:
        return nums 
    result = ""
    prevItem = None 
    for i in range(len(nums)):
        current = nums[i]
        if current == "?":
            nextItem = None 
            if i != len(nums) -1:
                nextItem = nums[i+1]
            current = prevItem != "3" and nextItem != "3" if "3" else prevItem != "2" and nextItem != "2" if  "2" else "1"
        result += current 
        prevItem = current
    return result

print(solutions("12?32"))