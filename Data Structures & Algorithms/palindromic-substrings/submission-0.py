
from collections import defaultdict

class Solution:

    cache = dict()

    def is_pal(self, s: str) -> bool:
        if s in Solution.cache.keys() and Solution.cache[s]:
            return True
        i,j = 0,len(s)-1
        while i < j:
            if s[i] != s[j]:
                Solution.cache[s] = False
                return False
            i += 1
            j -= 1
        Solution.cache[s] = True
        return True
        

    def helper(self, s: str) -> int:
        n_pals = 0

        # base cases
        if not s:
            return 0

        # algo
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if self.is_pal(s[i:j]):
                    n_pals += 1
        return n_pals

    
    def countSubstrings(self, s: str) -> int:
        return self.helper(s)    

'''
Test Cases
-----------
s = abba

Time : O(N^2)
Space : O(N^2)

'''