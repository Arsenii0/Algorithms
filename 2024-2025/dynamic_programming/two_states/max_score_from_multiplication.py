# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
# Remove x from nums.
# Return the maximum score after performing m operations.

 

# Example 1:

# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# Example 2:

# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(mult_index, left):
            if mult_index == len(multipliers):
                return 0

            if mult_index not in mem:
                mem[mult_index] = {}  
            
            if left not in mem[mult_index]:
                # mult_index is always +1
                # express right from left -> we need only 2 states
                right = (len(nums) - 1) - (mult_index - left)

                mem[mult_index][left] = max(dp(mult_index + 1, left + 1) + nums[left] * multipliers[mult_index],
                            dp(mult_index + 1, left) + nums[right] * multipliers[mult_index])

            return mem[mult_index][left]

        mem = {}
        return dp(0,0)
    

    # Bottom up (didn't finish)
    # def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    #     dp = {}
    #     nums_size = len(nums)
    #     mult_size = len(multipliers)

    #     # base case is when left == mult_index
    #     for mult_index in range(mult_size - 1, -1, -1):
    #         for left in range (mult_index, -1, -1):
    #             right = (nums_size - 1) - (mult_index - left)
    #             dp[mult_index][left] = 

    #     return dp(0,0)

    # top-down

        