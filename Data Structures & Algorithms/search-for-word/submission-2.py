'''
Notes
-----
1st attempt
-----------
- Failed several test cases
- Unable to find the bugs
- NeetBot identifed two bugs. See [Miss-1]

2nd attempt
-----------
- Fixed the two bugs
- Still only 5 test cases are passing
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base case(s)
        if not board or not word:
            return False

        # algo
        c = word[0]
        init_options = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == c:
                    init_options.append((i,j))
        
        if_exists = False
        for (i,j) in init_options:
            if_exists = if_exists | self.explore(board, i, j, word, 0)
        
        return if_exists


    def explore(self, board: List[List[str]], i: int, j: int, word: str, idx: int) -> bool:
        # base case(s)
        if idx == len(word):
            return False

        if idx == len(word) - 1 and 0 <=i < len(board) and 0 <= j < len(board[i]) and board[i][j] == word[idx]:
            return True

        # algo
        is_ok = False
        prev_char = board[i][j] 
        board[i][j] = '#' #[Miss-1]: Not tracking visited nodes
        options = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
        for (k,l) in options:
            # if k < len(board) and l < len(board[k]) and idx+1 < len(word): #[Miss-1] Check if k and l are not negative
            if 0 <= k < len(board) and 0 <= l < len(board[k]) and idx+1 < len(word):
                if board[k][l] == word[idx+1]:
                    if idx+1 == len(word) - 1: # last char matched
                        return True
                    is_option_ok = self.explore(board, k, l, word, idx+1)
                    is_ok = is_ok | is_option_ok
        board[i][j] = prev_char
        return is_ok