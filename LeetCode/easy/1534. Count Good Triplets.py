from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = []
        for i in range(0, (len(arr) - 1) - 2 + 1):
            for j in range(i + 1, (len(arr) - 1) - 1 + 1):
                for k in range(j + 1, (len(arr) - 1) + 1):
                    if abs(arr[i] - arr[j]) <= a \
                            and abs(arr[j] - arr[k]) <= b \
                            and abs(arr[i] - arr[k]) <= c:
                        answer.append((arr[i], arr[j], arr[k]))
        return len(answer)
