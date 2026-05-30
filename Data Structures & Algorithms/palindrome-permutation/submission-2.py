'''
Count char occurences
If each char ( except one ) occurs even no of times
'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # base case(s)
        if not s:
            return False

        # algo
        L = list(s)
        M = dict()
        for c in L:
            M[c] = M[c] + 1 if c in M else 1
        vals = list(M.values())
        singleton_found = False
        for val in vals:
            if val == 1 or val % 2 != 0:
                if singleton_found:
                    return False
                singleton_found = True
        return True
