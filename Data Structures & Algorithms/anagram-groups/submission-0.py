'''
Use a dict
group by sorted string


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case(s)
        if not strs:
            return []

        # code
        D = defaultdict(list)
        for s in strs:
            D[''.join(sorted(s))].append(s)
        res = []
        for k,v in D.items():
            res.append(v)
        return res  