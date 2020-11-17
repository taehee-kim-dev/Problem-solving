class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        words = s.split()
        for word in words:
            answer.append(word[::-1])

        return ' '.join(answer)
