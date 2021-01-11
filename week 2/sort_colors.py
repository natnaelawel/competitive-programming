def sort_colors(nums):
    sorted_array = [0, 0, 0]
    for i in range(len(nums)):
        sorted_array[nums[i]] += 1
    nums.clear()
    # for i in range(3):
    #     for j in range(sorted_array[i]):
    #         nums.append(i)
    nums = [i for i in range(3) for j in range(sorted_array[i])]
    return nums


print(sort_colors([2, 0, 2, 1, 1, 0]))
