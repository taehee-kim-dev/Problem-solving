from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums) - 2 + 1, 2):
            freq = nums[i]
            val = nums[i + 1]
            for _ in range(freq):
                answer.append(val)

        return answer
