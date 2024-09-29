class Solution:
    # top down
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1
            elif i not in mem:
                mem[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return mem[i]

        mem = {}
        return dp(n)

    # bottom uo
    # def tribonacci(self, n: int) -> int:
    #     dp = [0] * (n+1)
    #     dp[1] = 1
    #     dp[2] = 1
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    #     return dp[-1]
        