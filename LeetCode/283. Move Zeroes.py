from typing import List
import collections


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0
        count_non_zeros = 0
        index = 0
        while count_zeros + count_non_zeros < len(nums):
            if nums[index] == 0:
                count_zeros += 1
                nums.pop(index)
                nums.append(0)
            else:
                count_non_zeros += 1
                index += 1


Solution().moveZeroes([0, 1, 0, 3, 12])
