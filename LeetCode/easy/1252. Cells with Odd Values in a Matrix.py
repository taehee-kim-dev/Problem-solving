from typing import List
import collections


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        answer = 0
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        row_map = collections.defaultdict(int)
        col_map = collections.defaultdict(int)

        for row_to_increase, col_to_increase in indices:
            row_map[row_to_increase] += 1
            col_map[col_to_increase] += 1

        for row in row_map.keys():
            matrix[row] = [row_map[row] for _ in range(m)]

        for col in col_map.keys():
            for row in range(0, (n - 1) + 1):
                matrix[row][col] += col_map[col]

        for row in range(0, (n - 1) + 1):
            for col in range(m):
                if matrix[row][col] % 2 != 0:
                    answer += 1

        return answer



solution = Solution()
print(solution.oddCells(2, 2, [[1, 1], [0, 0]]))
