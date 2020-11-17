from typing import List
import collections

"""
일부가 포함 안된 것들의 합 < 일부의 합
여러개면, 사이즈가 최소인 것
사이즈가 최소인 것이 여러개면, 합이 제일 큰 것
답은 내림차순으로 반환.
"""


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        answer = []
        answer_sum = 0
        sorted_nums_deque = collections.deque(sorted(nums))
        deque_sum = sum(sorted_nums_deque)
        while sorted_nums_deque:
            pop_num = sorted_nums_deque.pop()
            answer.append(pop_num)
            answer_sum += pop_num
            deque_sum -= pop_num
            if answer_sum > deque_sum:
                return answer
