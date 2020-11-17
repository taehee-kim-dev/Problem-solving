from typing import List
import collections


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        check_map = collections.defaultdict(int)
        for num in A:
            check_map[num] += 1
            if check_map[num] == 2:
                return num
