class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        arr = []
        for n, cnt in freq.items():
            arr.append((cnt, n))
        arr.sort(reverse=True)

        print("SORTED", arr)

        res = []
        ctr = 0
        for cnt, n in arr:
            if ctr < k:
                res.append(n)
            ctr += 1
        return res