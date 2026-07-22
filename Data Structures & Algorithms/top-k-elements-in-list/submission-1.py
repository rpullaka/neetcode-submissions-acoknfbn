
import heapq
import itertools
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        counter = itertools.count()
        H = []
        for key,val in ctr.items():
            heapq.heappush(H, (val,next(counter),key))
            if len(H) > k:
                heapq.heappop(H)
        top_k = [key for _,_,key in H]
        return top_k