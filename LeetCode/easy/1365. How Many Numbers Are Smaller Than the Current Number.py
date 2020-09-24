from typing import *


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_map = dict()

        for i, num in enumerate(sorted(nums)):
            if num not in nums_map:
                nums_map[num] = i

        return [nums_map[num] for num in nums]


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
