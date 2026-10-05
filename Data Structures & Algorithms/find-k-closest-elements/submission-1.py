import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        x_ind = bisect.bisect_left(arr, x)
        l,r = x_ind, x_ind

        if x_ind < n and arr[x_ind] == x:
            k-=1
            l-=1
            r+=1
        else:
            l-=1
        
        for i in range(k):
            if r >= n:
                l-=1
            elif l<0:
                r+=1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l-=1
            else:
                r+=1
        res = []
        l += 1
        while l<r:
            res.append(arr[l])
            l+=1

        return res

        