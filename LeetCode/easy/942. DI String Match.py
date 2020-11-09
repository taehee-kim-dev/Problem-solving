from typing import List
import collections


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        answer = []
        nums_deque = collections.deque(list(range(0, len(S) + 1)))
        for char in S:
            if char == 'I':
                answer.append(nums_deque.popleft())
            else:
                answer.append(nums_deque.pop())

        answer.append(nums_deque.pop())
        return answer


print(Solution().diStringMatch('IDID'))
# [0,4,1,3,2]
print(Solution().diStringMatch('III'))
# [0,1,2,3]
print(Solution().diStringMatch('DDI'))
# [3,2,0,1]


