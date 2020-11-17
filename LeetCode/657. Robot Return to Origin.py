class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left_count = moves.count('L')
        right_count = moves.count('R')
        up_count = moves.count('U')
        down_count = moves.count('D')

        return left_count == right_count and up_count == down_count
