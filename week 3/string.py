def solution(nums):
    if nums == None or nums.index("?") == -1:
        return nums
    result = ""
    prevItem = None
    nextItem = None
    for i in range(len(nums)):
        current = nums[i]
        if current == "?":
            if i != len(nums) - 1:
                nextItem = nums[i+1]
            current = "1" if (prevItem != "1" and nextItem != "1") else "2" if (
                prevItem != "2" and nextItem != "2") else "1"
        result += str(current)
        prevItem = current
    return result


print(solution("1??3?3??"))
