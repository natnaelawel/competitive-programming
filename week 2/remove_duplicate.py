# %%
def removeDuplicates(nums):
    size = len(nums)
    i = 0
    while i < size-1:
        try:
            nextElm = nums[i+1]
        except:
            pass
        if nums[i] == nextElm:
            del nums[i]
            i = 0 if i == 0 else i - 1
            size -= 1

        else:
            i += 1

    return len(nums)


    # return len(nums)
nums = [1, 2, 2, 3, 4, 4, 5]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 1]
# nums = [0, 0, 0, 0, 0]
print(removeDuplicates(nums))
# %%
