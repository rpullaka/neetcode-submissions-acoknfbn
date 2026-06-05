'''
Go over each string
calculate a hash like string
Use a dict with this hash-like string as key
list out values key by key
time: O(N*M)
space: O(N*M)
'''

from collections import Counter
import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d2 = dict.fromkeys(string.ascii_lowercase, 0)
            for ch in s:
                d2[ch] += 1
            hash_key = "".join(f"{k}{v}" for k,v in d2.items())
            d[hash_key].append(s)
        res = []
        for k,v in d.items():
            res.append(v)
        return res