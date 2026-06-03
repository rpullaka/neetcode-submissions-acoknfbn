'''
Go over the shift matrix.
Sort by direction.
Add the amounts.
Find the final direction and amount.
Apply to the string.
'''

from collections import defaultdict

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # Add the amounts per direction
        D = defaultdict(int)
        for k,v in shift:
            D[k] += v
        
        # Final no of shifts. Positive means right shift. Negative means left shift.
        shifts = (D[0] - D[1]) % len(s)
        if shifts != 0:
            return s[shifts:] + s[:shifts]
        return s
