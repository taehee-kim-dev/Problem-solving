from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    answer += 1

        return answer


solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(solution.numIdenticalPairs([1, 1, 1, 1]))
print(solution.numIdenticalPairs([1, 2, 3]))

