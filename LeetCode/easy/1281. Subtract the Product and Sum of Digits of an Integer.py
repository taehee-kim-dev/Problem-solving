from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        product_of_digits = reduce(lambda result, number: result * number, digits)
        sum_of_digits = sum(digits)
        return product_of_digits - sum_of_digits


solution = Solution()
print(solution.subtractProductAndSum(234))
