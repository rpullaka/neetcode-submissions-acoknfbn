'''
06/17/2026
'''

'''
sort by start
consecutive intvls. merge and replace if overlapping

'''
class Solution:

    def is_valid(self, intvls: List[List[int]], idx: int) -> bool:
        if idx >= 0 and idx < len(intvls):
            return True
        return False

    def merge_intvl(self, intvls: List[List[int]], cur: int, nxt: int) -> None:
        if self.is_valid(intvls, cur) and self.is_valid(intvls, nxt):
            # new_intvl = [intvls[cur][0], intvls[nxt][1]] # [Miss] There's a bug here. What if the nxt interval is totally contained within the current interval.
            # [Weakpoint] Merge two lists efficiently
            new_vals = sorted([*intvls[cur], *intvls[nxt]])
            new_intvl = [new_vals[0], new_vals[-1]]
            intvls[cur] = new_intvl
            intvls.pop(nxt)

    def is_overlap(self, intvls: List[List[int]], cur: int, nxt: int) -> bool:
        if self.is_valid(intvls, cur) and self.is_valid(intvls, nxt):
            if intvls[cur][1] >= intvls[nxt][0]:
                return True
        return False


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # base
        if not intervals:
            return intervals

        # code
        sorted_intvls = sorted(intervals)
        (cur, nxt) = (0, 1)
        while self.is_valid(sorted_intvls, cur) and self.is_valid(sorted_intvls, nxt):
            if self.is_overlap(sorted_intvls, cur, nxt):
                self.merge_intvl(sorted_intvls, cur, nxt)
            else:
                cur += 1
                nxt += 1
        return sorted_intvls

'''
Test Cases

intvls = [[1,4], [3,6], [5,8]] => [[1,8]]

intvls = [[1,4]] => [[1,4]]

intvls = [[1,4], [5,8], [9,10]] => [[1,4], [5,8], [9,10]]
'''

'''
Complexity

Time : O(NlogN) + O(N*N) -> O(N^2)

Space : O(N)
'''