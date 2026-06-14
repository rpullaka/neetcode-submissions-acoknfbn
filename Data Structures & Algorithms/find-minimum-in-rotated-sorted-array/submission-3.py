class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case(s)
        if not nums:
            return -1

        # code
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r - l) // 2
            if nums[l] > nums[m]:
                r = m
            else:
                l = m+1
        return nums[l]