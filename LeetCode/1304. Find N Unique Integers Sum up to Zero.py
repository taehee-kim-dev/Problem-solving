from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for num in range(1, (n // 2) + 1):
            answer.append(num)
            answer.append(-num)

        if n % 2 != 0:
            answer.append(0)

        return answer
