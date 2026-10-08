class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        l, r = max(weights), sum(weights)

        sw_min = r

        def get_days_ws(ws: int):
            tdays = 1
            ts = 0
            for wt in weights:
                if (ts + wt) <= ws:
                    ts += wt
                    continue
                tdays += 1
                ts = wt
            return tdays


        while l <= r:
            m = (l+r)//2
            if get_days_ws(m) > days:
                l = m+1
            else:
                sw_min = min(sw_min, m)
                r = m-1

        return sw_min
