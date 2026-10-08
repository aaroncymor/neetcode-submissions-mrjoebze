class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def add_num(i, group, total):
            
            if total == target:
                res.append(group.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            group.append(nums[i])
            add_num(i, group, total + nums[i])
            group.pop()
            add_num(i + 1, group, total)
        
        add_num(0, [], 0)
        return res