from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num_str in list(map(str, nums)):
            if len(num_str) % 2 == 0:
                answer += 1

        return answer
