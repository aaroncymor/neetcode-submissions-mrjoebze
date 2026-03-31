class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, candidates, total):
            if target == total:
                res.append(candidates.copy())
                return
            
            if target < total or i >= len(nums):
                return
            
            candidates.append(nums[i])
            dfs(i, candidates, total + nums[i])
            candidates.pop()
            dfs(i + 1, candidates, total)
        
        dfs(0, [], 0)
        return res 