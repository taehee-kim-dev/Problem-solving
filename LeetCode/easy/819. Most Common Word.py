from typing import List
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]

        return collections.Counter(words).most_common(1)[0][0]







solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
