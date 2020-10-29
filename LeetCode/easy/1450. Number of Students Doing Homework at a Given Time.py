from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        studying_times = [[start_time, end_time] for start_time, end_time in zip(startTime, endTime)]
        return len([x for x in studying_times if x[0] <= queryTime <= x[1]])
