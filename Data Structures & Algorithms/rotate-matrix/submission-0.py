class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.mirror(matrix)

    def swap(self, matrix: List[List[int]], i, k, j, l) -> None:
        n = len(matrix)
        if i >= n or k >= n or j >= n or l >= n:
            return
        tmp = matrix[i][k]
        matrix[i][k] = matrix[j][l]
        matrix[j][l] = tmp

    def transpose(self, matrix: List[List[int]]) -> None:
        i = 0
        j = 0
        n = len(matrix)
        while i <= n and j <= n:
            k = i + 1
            l = j + 1
            while k <= n and l <= n:
                self.swap(matrix, i, k, l, j)
                k = k + 1
                l = l + 1
            i = i + 1
            j = j + 1
    
    def mirror(self, matrix: List[List[int]]) -> None:
        i = 0
        n = len(matrix)
        while i < n:
            j = 0
            k = n - 1
            while j < k:
                self.swap(matrix, i, j, i, k)
                j = j + 1
                k = k - 1
            i = i + 1
    