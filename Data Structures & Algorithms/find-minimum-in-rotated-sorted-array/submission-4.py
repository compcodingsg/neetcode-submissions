class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            m_l = nums[m-1] if m >0 else float("inf")
            m_r = nums[m+1] if m <len(nums)-1 else float("inf")
            if nums[m] < m_l and nums[m] < m_r:
                return nums[m]
            elif nums[m] >= nums[0] and nums[m] > nums[len(nums)-1]:
                l = m+1
            else:
                r=m-1
        
        