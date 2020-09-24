from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


solution = Solution()
solution.reverseString(["h", "e", "l", "l", "o"])
# ["o","l","l","e","h"]

solution = Solution()
solution.reverseString(["H", "a", "n", "n", "a", "h"])
# ["h","a","n","n","a","H"]
