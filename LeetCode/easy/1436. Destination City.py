from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set(x[0] for x in paths)

        for start, end in paths:
            if end not in start_cities:
                return end
