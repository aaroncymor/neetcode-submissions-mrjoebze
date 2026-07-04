class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, items, total):
            if total == target:
                res.append(items.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            items.append(nums[i])
            dfs(i, items, total + nums[i])
            items.pop()
            dfs(i + 1, items, total)
        
        dfs(0, [], 0)
        return res