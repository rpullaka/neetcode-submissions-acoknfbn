from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        ctr = Counter(nums)
        for val in ctr.values():
            if val > 1:
                return True
        return False