class Solution:

    def bin_search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l <= r:
            m = l + (r - l)//2
            if target == nums[m]:
                return True
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix and not matrix[0]:
            return False

        i,j,k,l = 0,len(matrix)-1,None,len(matrix[0])-1
        
        while i <= j:
            m = i + (j - i)//2
            if matrix[m][0] <= target <= matrix[m][l]:
                k = m
                break
            elif target < matrix[m][0]:
                j = m-1
            else:
                i = m+1
            
        
        if k is not None:
            return self.bin_search(matrix[k], target)
        
        return False
            

'''
1 2 3
4 5 6
7 8 9

Time : O(logM + logN)
Space : O(1)
'''
