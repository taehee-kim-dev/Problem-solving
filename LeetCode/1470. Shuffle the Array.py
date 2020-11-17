from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []

        for index_for_x in range(n):
            index_for_y = index_for_x + n
            x = nums[index_for_x]
            y = nums[index_for_y]
            answer.extend([x, y])

        return answer