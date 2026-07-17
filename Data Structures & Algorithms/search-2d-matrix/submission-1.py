class Solution:

    def bin_search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        if target in [nums[0], nums[len(nums)-1]]:
            return True

        l,r = 0,len(nums)-1
        while l < r:
            m = l + (r - l)//2
            if target == nums[m]:
                return True
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        k,l = None,len(matrix[0])-1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][l]:
                k = i
                break
        
        if k is not None:
            return self.bin_search(matrix[k], target)
        
        return False
            

'''
1 2 3
4 5 6
7 8 9

Time : O(M * logN)
Space : O(M)
'''
