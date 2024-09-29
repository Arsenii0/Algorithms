class Solution:
    #Top down
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            elif i not in mem:
                # It can't be dp(i - 1) + nums[i] because THE PREVIOUS HOUSE MUST not be robbed
                mem[i] = max(dp(i-1), dp(i-2) + nums[i])
            return mem[i]

        mem = {}
        return dp(len(nums) - 1)

# bottom-up
#     def rob(self, nums: List[int]) -> int:
#         dp = [0] * len(nums)

#         dp[0] = nums[0]
#         dp[1] = max (nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
#         return dp[-1]