class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num * -1)

        if (
            (self.small and self.large) and
            (self.small[0] * -1 > self.large[0])
        ):
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)
        elif len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)

    def findMedian(self) -> float:

        if not self.small and not self.large:
            return 0

        if len(self.small) > len(self.large):
            return self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0] * -1
        
        return (self.small[0] + (self.large[0] * -1)) / 2.0
        
        