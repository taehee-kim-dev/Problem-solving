from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(0, len(nums) - 1 + 1):
            answer.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            answer[i] *= p
            p *= nums[i]

        return answer

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
# [24, 12, 8, 6]
