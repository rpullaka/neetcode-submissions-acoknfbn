'''
Notes
-----
06/26/26

1st attempt: Ran the code and all test case failed. There seems to be a bug somewhere.

'''

class Solution:

    def helper(self, nums: List[int], idx: int, bag: List[List[int]]) -> None:
        # base
        if idx == len(nums):
            bag.append(list(nums))
            return

        # algo
        # for i in range(idx+1,len(nums)):
        for i in range(idx,len(nums)):
            temp = nums[idx]
            nums[idx] = nums[i]
            nums[i] = temp
            self.helper(nums, idx+1, bag)
            temp = nums[idx]
            nums[idx] = nums[i]
            nums[i] = temp
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        bag  =list()

        # base
        if not nums:
            return list()

        # algo
        self.helper(nums, 0, bag)

        return bag

'''
Test Cases
----------
nums = [1, 2, 3, 4]
nums = [1]


Time: O(N!)
Space: O(N!)

'''       