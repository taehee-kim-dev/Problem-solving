class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        answer = ''
        left_parentheses_not_matched = 0
        tmp = ''
        for char in S:
            tmp += char

            if char == '(':
                left_parentheses_not_matched += 1
            else:
                left_parentheses_not_matched -= 1

            if left_parentheses_not_matched == 0:
                answer += tmp[1:-1]
                tmp = ''

        return answer
