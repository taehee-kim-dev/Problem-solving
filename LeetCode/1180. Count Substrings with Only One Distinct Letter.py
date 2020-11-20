import re


class Solution:
    def countLetters(self, S: str) -> int:
        S_disticts = list(set(S))

        for char in S_disticts:
            p = re.compile(char + '+')
            matched_strings = p.findall(S)
            print(matched_strings)


Solution().countLetters("aaaba")
