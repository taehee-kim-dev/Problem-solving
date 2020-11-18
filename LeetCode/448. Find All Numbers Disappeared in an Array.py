from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        all_numbers = set(range(1, len(nums) + 1))
        nums = set(nums)
        return list(all_numbers - nums)
