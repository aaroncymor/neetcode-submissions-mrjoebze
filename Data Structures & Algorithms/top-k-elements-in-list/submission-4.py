class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        return [num for count, num in heap]
