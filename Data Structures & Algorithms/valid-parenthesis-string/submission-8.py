
from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        if not s:
            return False 
    
        left = deque()
        star = deque()
        for (i,ch) in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            elif ch == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                return False
        
        while left and star and left[-1] < star[-1]:
            left.pop()
            star.pop()
        
        if not left:
            return True

        return False

'''
Test Cases

s = (((*)))

s = ((((*))
'''
        