
'''
create a counter. compare them

T: O(N)
S: O(N)
'''

'''
Notes
-----
- Don't know what Counter(None) or Counter('') would be. Had to check.
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base


        # code
        s_c = Counter(s)
        t_c = Counter(t)

        return s_c == t_c