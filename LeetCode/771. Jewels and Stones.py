
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        answer = 0
        for j in J:
            answer += S.count(j)

        return answer

solution = Solution()
print(solution.numJewelsInStones(J = "aA", S = "aAAbbbb"))
print(solution.numJewelsInStones(J = "z", S = "ZZ"))
