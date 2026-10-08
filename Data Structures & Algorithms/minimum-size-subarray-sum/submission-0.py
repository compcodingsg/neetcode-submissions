class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        res = n+1
        s = 0
        l, r = 0, 0

        while r < n:
            s += nums[r]
            if s >= target:
                while s >= target:
                    res = min(res, r-l+1)
                    s -= nums[l]
                    l += 1
            r += 1
        
        return res if res <= n else 0


