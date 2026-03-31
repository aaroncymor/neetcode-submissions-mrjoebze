class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        heap = []

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, n))
            elif heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, n))
        
        return [n for count, n in heap]

