class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = set()
        n = len(nums)
        k = min(k+1, n)

        for i in range(k):
            ele = nums[i]
            if ele in lookup:
                return True
            lookup.add(ele)
        
        i = k
        while i<n:
            ele = nums[i]
            lookup.remove(nums[i-k])
            if ele in lookup:
                return True
            lookup.add(ele)
            i+=1
        
        return False
            