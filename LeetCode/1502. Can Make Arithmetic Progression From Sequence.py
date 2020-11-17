from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr:
            return True

        sorted_arr = sorted(arr)
        first_num = sorted_arr[0]
        second_num = sorted_arr[1]
        diff = second_num - first_num
        arithmetic_nums = [first_num]
        while len(arithmetic_nums) < len(arr):
            arithmetic_nums.append(arithmetic_nums[-1] + diff)
        print(arithmetic_nums)
        return sorted_arr == arithmetic_nums

