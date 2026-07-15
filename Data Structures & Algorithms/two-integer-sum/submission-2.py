'''
07/15/26

Better than brute force

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        A = []
        for i,a in enumerate(nums):
            A.append([a,i])
        
        A.sort()

        i,j = 0,len(A)-1
        while i < j:
            val = A[i][0] + A[j][0]
            if val == target:
                return sorted([A[i][1],A[j][1]])
            elif val < target:
                i += 1
            else:
                j -= 1
        return []

'''
Time: O(NlogN)
Space: O(N) 
'''
