from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        positive_or_zero = 0
        negative_start_col = len(grid[0])
        for row_index in range(len(grid)):
            col_index = 0
            while col_index < negative_start_col:
                if grid[row_index][col_index] >= 0:
                    positive_or_zero += 1
                else:
                    negative_start_col = col_index
                col_index += 1

        return (len(grid) * len(grid[0])) - positive_or_zero


print(Solution().countNegatives([[5, 1, 0], [-5, -5, -5]]))
