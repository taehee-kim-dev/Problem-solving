from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row_index in range(0, (len(A) - 1) + 1):
            A[row_index] = [0 if x == 1 else 1 for x in A[row_index][::-1]]

        return A
