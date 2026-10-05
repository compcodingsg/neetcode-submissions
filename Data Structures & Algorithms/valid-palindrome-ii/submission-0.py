class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        def is_pallindrome(l: int, r: int):
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
            
        while l<r:
            if s[l] != s[r]:
                return is_pallindrome(l+1,r) or is_pallindrome(l,r-1)
            l,r = l+1, r-1
        return True