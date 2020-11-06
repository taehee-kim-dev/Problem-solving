from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if 0 < i and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    # 정답인 경우
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer





solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
# [[-1,-1,2],[-1,0,1]]

print(solution.threeSum([]))
# []

print(solution.threeSum([0]))
# []


