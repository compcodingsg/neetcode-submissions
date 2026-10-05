class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ui = 1
        i = 1
        n = len(nums)

        while i<n:
            if nums[i] != nums[i-1]:
                nums[ui] = nums[i]
                ui += 1
            i += 1
        return ui                
