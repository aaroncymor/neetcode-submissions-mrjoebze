class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        minHeap = []
        for num, count in freq.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, num))
            elif minHeap[0][0] < count:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (count, num))
        
        return [num for count, num in minHeap]
