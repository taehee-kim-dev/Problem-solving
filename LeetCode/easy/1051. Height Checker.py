from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        for original_student, sorted_student in zip(heights, sorted(heights)):
            if original_student != sorted_student:
                answer += 1
        return answer
