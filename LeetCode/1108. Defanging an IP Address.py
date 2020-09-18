
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')






solution = Solution()
print(solution.defangIPaddr('1.1.1.1'))
print(solution.defangIPaddr('255.100.50.0'))
