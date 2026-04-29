class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 0:
            total = sum(self.heap)
            return total / 2.0
        mid = len(self.heap) // 2
        return self.heap[mid]
        
        