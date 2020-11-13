from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        answer = 0
        tmp_chars = []
        for chars in zip(*A):
            tmp_chars.append(chars)
        sorted_tmp_chars = list(map(lambda x: tuple(sorted(x)), tmp_chars))
        for original_chars, sorted_chars in zip(tmp_chars, sorted_tmp_chars):
            if original_chars != sorted_chars:
                answer += 1

        return answer
