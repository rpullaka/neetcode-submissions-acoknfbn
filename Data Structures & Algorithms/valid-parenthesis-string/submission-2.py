from functools import lru_cache
class Solution:
    
    @lru_cache(None)
    def checker(self, s: str, idx: int, l_c: int, r_c: int) -> bool:
        # base case(s)
        if l_c < r_c:
            return False
        
        if idx == len(s):
            if l_c == r_c:
                return True
            return False

        # code
        val1 = val2 = val3 = val4 = val5 = False

        if s[idx] == '(':
            val1 = self.checker(s, idx+1, l_c + 1, r_c)
        
        elif s[idx] == ')':
            val2 = self.checker(s, idx+1, l_c, r_c + 1)
        
        elif s[idx] == '*':
            val3 = self.checker(s, idx+1, l_c, r_c) # empty char
            val4 = self.checker(s, idx+1, l_c + 1, r_c) # left bracket
            val5 = self.checker(s, idx+1, l_c, r_c + 1) # right bracket
        
        if val1 or val2 or val3 or val4 or val5:
            return True
        
        return False


    
    def checkValidString(self, s: str) -> bool:
        # base case(s)
        if s == None:
            return False

        if s == '':
            return True

        if s and s[0] == ')':
            return False

        return self.checker(s, 0, 0, 0)