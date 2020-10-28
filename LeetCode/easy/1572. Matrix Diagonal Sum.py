from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        # primary
        for i in range(0, len(mat) - 1 + 1):
            answer += mat[i][i]

        # secondary
        for i in range(0, len(mat) - 1 + 1):
            j = len(mat) - 1 - i
            if i == j:
                continue
            answer += mat[i][j]

        return answer
