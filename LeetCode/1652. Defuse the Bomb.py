from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        if k == 0:
            return [0 for _ in range(len(code))]
        elif 0 < k:
            for code_num_i in range(0, len(code)):
                searching_i = code_num_i + 1
                tmp_sum = 0
                tmp_k = k
                while tmp_k > 0:
                    if searching_i >= len(code):
                        searching_i = 0
                    tmp_sum += code[searching_i]
                    tmp_k -= 1
                    searching_i += 1
                answer.append(tmp_sum)
        else:
            for code_num_i in range(0, len(code)):
                searching_i = code_num_i - 1
                tmp_sum = 0
                tmp_k = -k
                while tmp_k > 0:
                    if searching_i < 0:
                        searching_i = len(code) - 1
                    tmp_sum += code[searching_i]
                    tmp_k -= 1
                    searching_i -= 1
                answer.append(tmp_sum)

        return answer


print(Solution().decrypt([2,4,9,3], -2))
