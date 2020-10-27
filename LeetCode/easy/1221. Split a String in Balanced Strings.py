class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        count_L = 0
        count_R = 0

        for c in s:
            if c == 'L':
                count_L += 1
            else:
                count_R += 1

            if (count_L >= 1 and count_R >= 1) \
                and (count_L == count_R):
                answer += 1
                count_L = 0
                count_R = 0

        return answer
