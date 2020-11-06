from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_largest_num = 0
        second_largest_num = 0
        for num in nums:
            if num > first_largest_num:
                first_largest_num, second_largest_num = num, first_largest_num
            else:
                second_largest_num = max(second_largest_num, num)

        return (first_largest_num - 1) * (second_largest_num - 1)

