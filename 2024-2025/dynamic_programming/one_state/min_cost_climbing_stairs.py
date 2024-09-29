class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i == 0 or i == 1:
                return 0
            elif i not in mem:
                step_one = dp(i-1) + cost[i-1]
                step_two = dp(i-2) + cost[i-2]
                mem[i] = min(step_one, step_two)
            return mem[i]
            
        mem = {}

        # len(cost) represents the position just after the last step. Since you can either step
        # from the last step (len(cost) - 1) or the second-to-last step (len(cost) - 2)
        # to reach the top, you need to calculate the minimum cost to get to the
        # position just beyond the last step (len(cost)). 

        # So, you want to calculate the cost to reach this position,
        # which could involve stepping from either of the last two steps.
        result = dp(len(cost))

        return result

    # bottom-up    
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     dp = [0] * (len(cost) + 1)
    #     for i in range (2, len(cost) + 1):
    #         step_one = dp[i-1] + cost[i-1]
    #         step_two = dp[i-2] + cost[i-2]
    #         dp[i] = min(step_one, step_two)

    #     return dp[-1]
        