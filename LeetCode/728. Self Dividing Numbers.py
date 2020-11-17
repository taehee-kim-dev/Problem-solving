from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_self_dividing_number(number: int) -> bool:
            if '0' in str(number):
                return False

            for digit_char in str(number):
                if number % int(digit_char) != 0:
                    return False

            return True

        answer = []
        for num in range(left, right + 1):
            if is_self_dividing_number(num):
                answer.append(num)

        return answer
