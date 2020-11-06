from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        index_stack = []
        for i, price in enumerate(prices):
            while index_stack and prices[index_stack[-1]] >= price:
                prices[index_stack.pop()] -= price
            index_stack.append(i)
        return prices
