from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], cur_max = cur_max, max(arr[i], cur_max)
        return arr


Solution().replaceElements([17, 18, 5, 4, 6, 1])
