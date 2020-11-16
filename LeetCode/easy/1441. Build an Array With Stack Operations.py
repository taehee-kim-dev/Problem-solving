from typing import List
import collections


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        arr = []
        cur_list = collections.deque(range(1, n + 1))
        cur_arr_index = -1
        while arr != target:
            arr.append(cur_list.popleft())
            cur_arr_index += 1
            answer.append('Push')
            if arr[cur_arr_index] != target[cur_arr_index]:
                arr.pop()
                answer.append('Pop')
                cur_arr_index -= 1

        return answer


print(Solution().buildArray([1, 3], 3))
