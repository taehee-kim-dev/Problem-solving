from typing import *


class Solution:
    def numberOfSteps(self, num: int) -> int:
        number_of_steps = 0
        while num != 0:
            number_of_steps += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return number_of_steps


solution = Solution()
print(solution.numberOfSteps(14))
print(solution.numberOfSteps(8))
print(solution.numberOfSteps(123))
print(solution.numberOfSteps(0))
