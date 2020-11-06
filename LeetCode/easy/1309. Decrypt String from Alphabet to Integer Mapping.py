class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''

        i = 0
        while i <= len(s) - 1:
            if i + 2 <= len(s) - 1 and s[i + 2] == '#':
                answer += self.convert(s[i:(i + 1) + 1])
                i += 3
            else:
                answer += self.convert(s[i])
                i += 1

        return answer

    def convert(self, pure_number_str):
        return str(chr((ord('a') - 1) + int(pure_number_str)))


Solution().freqAlphabets('asdf')

