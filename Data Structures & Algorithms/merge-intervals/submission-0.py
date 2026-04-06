'''
Questions
---------
1. Can the interval array be empty
2. Assuming "end_i" is always greater than or equal to "start_i"
'''

'''
Approach-1
----------
1. Sort the intervals based on "start_i"
2. Look at consecutive intervals one by one. 
    2.1. If the intervals can be merged ( meaning 2nd interval's start falls in the 1st interval ) merge the two intervals. Keep going.
    2.2. If the intervals cannot be merged ( meaning 2nd interval's start falls outside the 1st interval ), don't do anything and move the 1st interval pointer right.  
3. Move the 2nd interval pointer right.
4. Do (2) and (3) till the 2nd interval reaches None. 
'''

'''
Learnings
---------
1. Use sorted(intervals, key=lambda x: x[0]) to sort a list of lists based on 1st element in the sublist while not altering the original list.
2. Naming variables is taking lot of time. It shouldn't.
3. How to remove two consecutive objects from a list and insert a new object in the same place?
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort the intervals based on "start_i"
        intvs = sorted(intervals, key=lambda x: x[0])
        cur = 0
        while cur < len(intvs) - 1:
            if intvs[cur][0] <= intvs[cur + 1][0] <= intvs[cur][1]:
                # 2.1. If intervals can be merged
                intvs[cur][1] = max(intvs[cur][1], intvs[cur + 1][1])
                del intvs[cur + 1]
            else:
                # 2.2. Look at next one
                cur += 1
        return intvs