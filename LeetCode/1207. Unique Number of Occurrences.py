from typing import List
import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        return len(counter) == len(set(counter.values()))

