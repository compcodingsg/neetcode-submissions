from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        if not values:
            return ""
        l,r = 0,len(values)-1

        while l<r:
            m = min((l+r+1)//2,r)
            if values[m][1] > timestamp:
                r = m-1
            else:
                l = m
            
        return values[l][0] if values[l][1] <= timestamp else ""


