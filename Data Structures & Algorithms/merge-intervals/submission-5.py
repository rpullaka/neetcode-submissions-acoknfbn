'''
07/23/26

Totally buggy

'''

from collections import defaultdict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        table = defaultdict(int)
        for start,end in intervals:
            table[start] += 1
            table[end] -= 1 
        
        keys = sorted(table.keys())
        
        new_intvls = []
        cur_intvl = []
        active_intvls = 0
        for key in keys:
            if not cur_intvl:
                cur_intvl.append(key)
            # else:
            #     cur_intvl[-1] = key
            active_intvls += table[key]
            if active_intvls == 0:
                cur_intvl.append(key)
                new_intvls.append(cur_intvl)
                cur_intvl = []
        return new_intvls