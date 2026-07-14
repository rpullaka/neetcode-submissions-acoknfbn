
'''
07/14/2026

Cleaned up Solution 2

'''

class Solution:

    def helper(self, nums: List[int], i: int, j: int, memo: List[List], sum_sofar: int) -> int:

        if i == j:
            return max(sum_sofar, nums[i])

        # Algo
        memo[i][j] = sum_sofar
        max1 = max2 = max3 = sum_sofar
        if i < j:
            max1 = memo[i+1][j] if memo[i+1][j] else self.helper(nums, i+1, j, memo, sum_sofar - nums[i])
            max2 = memo[i][j-1] if memo[i][j-1] else self.helper(nums, i, j-1, memo, sum_sofar - nums[j])

        return max(max1, max2, max3, sum_sofar)




    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        memo = [[None] * len(nums) for _ in range(len(nums))]

        return self.helper(nums, 0, len(nums)-1, memo, sum(nums))

'''

'''
