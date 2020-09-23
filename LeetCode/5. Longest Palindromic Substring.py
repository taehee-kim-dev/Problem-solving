
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            # 일단 확장 시도
            while 0 <= left and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            # 확장 실패하면, 확장 직전 문자열로 반환
            return s[left + 1:right]

        # 이미 팰린드롬이면 바로 입력 문자열 반환
        if s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            # 길이가 가장 긴 팰린드롬 문자열 저장.
            result = max(result, expand(i, i), expand(i, i + 1), key=len)

        return result



solution = Solution()
print(solution.longestPalindrome("dddd"))
