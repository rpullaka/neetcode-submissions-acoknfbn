from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        def bfs(cell: tuple) -> None:
            Q = deque([cell])
            while Q:
                (i,j) = Q.popleft()
                # grid[i][j] = "#"
                neighbors = ((i+1,j),(i-1,j),(i,j+1),(i,j-1))
                for (k,l) in neighbors:
                    if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] == "1":
                        grid[k][l] = "#"
                        Q.append((k,l))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    n_islands += 1
                    bfs((i,j))
        
        return n_islands

'''
Time: O(V*4)
Space: O(V)
'''