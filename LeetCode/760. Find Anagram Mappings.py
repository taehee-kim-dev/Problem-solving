from typing import List


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        answer = []
        for a in A:
            answer.append(B.index(a))

        return answer
