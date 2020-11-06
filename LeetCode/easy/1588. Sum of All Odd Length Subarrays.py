from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        for start_i in range(len(arr) - 1 + 1):
            end_i = start_i
            tmp_sum = 0
            while end_i <= len(arr) - 1:
                tmp_sum += arr[end_i]
                if start_i < end_i:
                    tmp_sum += arr[end_i - 1]
                answer += tmp_sum
                end_i += 2

        return answer


solution = Solution()
print(solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
