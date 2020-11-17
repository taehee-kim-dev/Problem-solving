from typing import List
import collections


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        odds = collections.deque()
        evens = collections.deque()

        for num in A:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        answer = []
        for i in range(len(A)):
            if i % 2 == 0:
                answer.append(evens.popleft())
            else:
                answer.append(odds.popleft())

        return answer


Solution().sortArrayByParityII([4,2,5,7])
