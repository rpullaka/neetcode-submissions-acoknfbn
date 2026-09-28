class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        comb = []
        combs = []
        def dfs(i: int, sum_so_far: int):
            if i >= len(nums):
                return
            if sum_so_far > target:
                return
            if sum_so_far == target:
                combs.append(comb.copy())
                return
            comb.append(nums[i])
            dfs(i, sum_so_far + nums[i])
            comb.pop()
            dfs(i+1, sum_so_far)
        dfs(0,0)
        return combs