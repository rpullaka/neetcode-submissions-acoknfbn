'''
build a hash table
sort the items by value
list the top K

T: O(N) + O(NlogN) + O(K)
S: O(N)

==============================

build a hash table of element counts
build a reverse index of count -> [elements]
return the top K from the reverse index

T : O(N) + O(N)
S : O(N)
'''
from collections import Counter, defaultdict, deque
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # base case(s)
        if not nums:
            return []

        # code
        index = Counter(nums)
        # rev_index = defaultdict(deque)
        rev_index = [deque() for _ in range(len(nums) + 1)]
        [rev_index[v].append(k) for k,v in index.items()]
        top_k = []
        # map(lambda d: top_k.extend(d), rev_index[-k:])

        for d in reversed(rev_index):
                if len(top_k) >= k:
                    break
                top_k.extend(d)
        return top_k[:k]