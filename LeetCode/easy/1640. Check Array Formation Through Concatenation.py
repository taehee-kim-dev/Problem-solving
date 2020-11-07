from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {piece[0]: piece for piece in pieces}
        result = []
        for num in arr:
            result += mapping.get(num, [])
        return result == arr


Solution().canFormArray([49, 18, 16], [[16, 18, 49]])
