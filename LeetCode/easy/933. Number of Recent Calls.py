import bisect


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return len(self.requests) - bisect.bisect_left(self.requests, t - 3000)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
