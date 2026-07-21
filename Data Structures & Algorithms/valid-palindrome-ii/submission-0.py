class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
            
        def is_pal(s: str, l: int, r: int) -> bool:
            i,j = l,r
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l,r = 0,len(s)-1
        while l < r:
            if s[l] != s[r]:
                return is_pal(s, l+1, r) or is_pal(s, l, r-1)
            l += 1
            r -= 1
        return True