class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_arr(l: int, r: int):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        n = len(nums)
        reverse_arr(0, n-1)
        reverse_arr(0, k%n-1)
        reverse_arr(k%n, n-1)