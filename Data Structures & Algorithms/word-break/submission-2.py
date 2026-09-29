class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}
        def is_valid(ss: str) -> bool:
            if not ss:
                return True
            if ss in memo:
                return memo[ss]
            for i in range(1, len(ss) + 1):
                if ss[:i] in word_set and is_valid(ss[i:]):
                    memo[ss] = True
                    return True
            memo[ss] = False
            return False
        return is_valid(s)