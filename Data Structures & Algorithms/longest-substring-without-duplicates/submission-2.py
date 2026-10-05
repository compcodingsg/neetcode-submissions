class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        lols = 0
        window = {}
        for r in range(n):
            if s[r] in window and window[s[r]] >= l:
                l = window[s[r]] + 1
            window[s[r]] = r
            lols = max(lols, r-l+1)
        return lols