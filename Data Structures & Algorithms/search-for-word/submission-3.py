class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        memo = set()
        rows,cols = len(board),len(board[0])

        def dfs(r, c, i) -> bool:
            if i == len(word):
                return True
            
            if (min(r,c) < 0 or r >= rows or c >= cols or ((r,c) in memo)):
                return False

            if board[r][c] == word[i]:
                memo.add((r, c))
                options = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
                exists = False
                for (r_n, c_n) in options:
                    exists |= dfs(r_n, c_n, i+1)
                    if exists:
                        return True
                memo.remove((r, c))
            return False
        
        exists = False
        for i in range(rows):
            for j in range(cols):
                exists |= dfs(i, j, 0)
                if exists == True:
                    return True
        return False
                    