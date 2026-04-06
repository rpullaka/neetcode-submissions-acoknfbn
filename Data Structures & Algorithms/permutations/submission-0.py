class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        bag = []
        self.helper(nums, 0, bag)
        return bag

    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def helper(self, nums: List[int], idx: int, bag: List[List[int]]):
        if idx == len(nums):
            bag.append(nums.copy())
            return

        for i in range(idx+1):
            self.swap(nums, idx, i)
            self.helper(nums, idx + 1, bag)
            self.swap(nums, idx, i)