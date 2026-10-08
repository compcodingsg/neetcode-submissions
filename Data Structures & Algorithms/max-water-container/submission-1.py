class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ma = 0
        n = len(heights)

        l,r = 0, n-1

        while l < r:
            ma = max(ma, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ma
        