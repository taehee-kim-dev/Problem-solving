from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counter = collections.Counter(nums)
        for num, count in counter.items():
            if count == 1:
                return num
