from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        before_x, before_y = points[0][0], points[0][1]
        for current_x, current_y in points[1:]:
            answer += max(abs(current_x - before_x), abs(current_y - before_y))
            before_x, before_y = current_x, current_y
        return answer
