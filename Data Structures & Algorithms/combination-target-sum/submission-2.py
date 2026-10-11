class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def dfs(curr: int, t: int):
            if t == 0:
                return [[]]
            if curr == len(nums):
                return []
            if nums[curr] > t:
                return []

            
            res = []
            for i in range((t//nums[curr])+1):
                dfsi = dfs(curr+1, t - nums[curr]*i)
                for pw in dfsi:
                    res.append(pw+[nums[curr]]*i)
            
            return res
        nums.sort()
        return dfs(0,target)
        