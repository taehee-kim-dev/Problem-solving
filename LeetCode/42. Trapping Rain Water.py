from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        volume = 0
        left_index, right_index = 0, len(height) - 1
        left_max_height, right_max_height = height[left_index], height[right_index]
        while left_index < right_index:
            left_max_height = max(left_max_height, height[left_index])
            right_max_height = max(right_max_height, height[right_index])

            if left_max_height <= right_max_height:
                volume += left_max_height - height[left_index]
                left_index += 1
            else:
                volume += right_max_height - height[right_index]
                right_index -= 1

        return volume


solution = Solution()
print(solution.trap([]))
# 6
