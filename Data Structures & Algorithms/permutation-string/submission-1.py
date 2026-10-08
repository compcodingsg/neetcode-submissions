from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        mp = defaultdict(int)

        for ch in s1:
            mp[ch] += 1

        l, r = 0,0

        while r < m:
            # add ele to window
            mp[s2[r]] -= 1
            if mp[s2[r]] == 0:
                del mp[s2[r]]
            
            if (r-l+1) < n:
                r += 1
                continue
            
            if len(mp) == 0:
                return True
            
            mp[s2[l]] += 1
            if mp[s2[l]] == 0:
                del mp[s2[l]]
            
            l += 1
            r += 1
             
        return False
            
            
