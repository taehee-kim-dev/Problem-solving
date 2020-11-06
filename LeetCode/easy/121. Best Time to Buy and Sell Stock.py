from typing import *
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price > min_price and price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
# 5

print(solution.maxProfit([7, 6, 4, 3, 1]))
# 0
