class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = set()
        l = 0
        for r in range(len(nums)):
            if r -l > k:
                lookup.remove(nums[l])
                l+=1
            if nums[r] in lookup:
                return True
            lookup.add(nums[r])
        return False