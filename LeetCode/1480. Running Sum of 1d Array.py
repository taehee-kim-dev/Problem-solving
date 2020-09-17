from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum_tmp = 0
        for num in nums:
            sum_tmp += num
            result.append(sum_tmp)

        return result


solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))
