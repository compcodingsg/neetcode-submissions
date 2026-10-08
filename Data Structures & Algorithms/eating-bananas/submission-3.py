class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        k_min = max(piles)
        l,r = 1, k_min
        

        def total_time_k(k: int):
            return sum([(pile + k - 1)//k for pile in piles])

        while l <= r:
            m = (l+r)//2
            if total_time_k(m) > h:
                l = m + 1
            else:
                k_min = min(k_min, m)
                r = m - 1
        
        return k_min


