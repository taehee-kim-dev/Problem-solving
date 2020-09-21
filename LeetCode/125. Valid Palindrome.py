import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_lower: str = s.lower()
        s_pure: str = re.sub('[^a-z0-9]', '', s_lower)

        return s_pure == s_pure[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
