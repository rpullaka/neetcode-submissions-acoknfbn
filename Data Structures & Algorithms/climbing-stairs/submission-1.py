class Solution:
    memo = dict()
    
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0

        elif n == 0:
            return 1

        res = 0
        res += self.memo[n-1] if n-1 in self.memo else self.climbStairs(n-1)
        res += self.memo[n-2] if n-2 in self.memo else self.climbStairs(n-2)

        self.memo[n] = res

        return res