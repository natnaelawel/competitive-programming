class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        for i in range(len(nums)):
            max_ = max(nums[i:])
            if nums[i] == max_:
                continue
            last_index = len(nums) - nums[i:][::-1].index(max_)-1 # last index
            nums[last_index], nums[i] = nums[i], nums[last_index]
            break
        return int("".join(list(map(str, nums))))