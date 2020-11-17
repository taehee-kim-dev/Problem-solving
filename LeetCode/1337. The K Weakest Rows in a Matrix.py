from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        row_index_soldiers = []
        for row_index, row, in enumerate(mat):
            row_index_soldiers.append((row_index, row.count(1)))

        row_index_soldiers.sort(key=lambda x: (x[1], x[0]))

        answer = []
        for row_inform in row_index_soldiers[:k]:
            answer.append(row_inform[0])

        return answer

