from typing import *


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_with_index = []
        for i, char in zip(indices, s):
            s_with_index.append((i, char))

        s_with_index.sort(key=lambda x: x[0])
        answer = ''
        for char_with_index in s_with_index:
            answer += char_with_index[1]

        return answer



solution = Solution()
print(solution.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
# "leetcode"
