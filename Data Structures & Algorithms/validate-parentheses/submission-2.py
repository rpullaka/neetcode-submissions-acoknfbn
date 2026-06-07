'''
Approach
--------
use a stack
go char by char
push open brace if found
pop open brace if a matching close brace found
stack should be empty 
'''

'''
Weak points
-----------
- Tried to access last element in a deque using top = stk[-1] which is wrong. Need to check first if the deque is not empty.

'''

'''
Notes
-----
- A major bug in the first attempt.
'''

from collections import deque, Counter
class Solution:
    def isValid(self, s: str) -> bool:
        # base case(s)
        if not s:
            return False

        ctr = Counter(s)
        if ctr[')'] > ctr['('] or ctr['}'] > ctr['{'] or ctr[']'] > ctr['[']:
            return False
            
        # code
        stk = deque()
        for c in s:
            top = stk[-1] if stk else ''
            if c in ['(', '{', '[']:
                stk.append(c)
            elif c == ')' and top == '(':
                stk.pop()
            elif c == '}' and top == '{':
                stk.pop()
            elif c == ']' and top == '[':
                stk.pop()
        if not stk:
            return True
        return False