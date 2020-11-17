from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        max_number_of_candies = max(candies)
        for number_of_candy in candies:
            if number_of_candy + extraCandies >= max_number_of_candies:
                answer.append(True)
            else:
                answer.append(False)

        return answer