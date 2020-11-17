from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        row_min_positions = []
        col_max_positions = []

        m = len(matrix)
        n = len(matrix[0])
        for row_i in range(0, m):
            row_min_num = min(matrix[row_i])
            row_min_positions.append((row_i, matrix[row_i].index(row_min_num)))

        for col_i in range(0, n):
            col_nums = []
            for row_i in range(0, m):
                col_nums.append(matrix[row_i][col_i])
            col_max_num = max(col_nums)
            col_max_positions.append((col_nums.index(col_max_num), col_i))

        common_positions = list(set(row_min_positions) & set(col_max_positions))
        for position in common_positions:
            answer.append(matrix[position[0]][position[1]])

        return answer

