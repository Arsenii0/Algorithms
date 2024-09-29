# You are given an integer array nums. You want to maximize the number of points you get by performing the 
# following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and
# every element equal to nums[i] + 1. Return the maximum number of points you can earn
# by applying the above operation some number of times.

 

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cost_per_num = defaultdict(int)
        max_num = nums[0]
        for num in nums:
            # Cost per num = how many points for each number specifically
            cost_per_num[num] += num
            max_num = max(max_num, num)

        # i is a number. We "interate" from 0 to max_number. We need to consider all from 0 to max_number
        # because we need i-1 and i+1. If i-1 or i+1 not in cost_per_num, cost_per_num simply returns 0
        def dp(i):
            if i == 0:
                return 0
            elif i == 1:
                return cost_per_num[1]
            elif i not in mem:
                # only i - 1 because it also includes i + 1 if we go forward/backwards
                mem[i] = max(dp(i-1), dp(i-2) + cost_per_num[i]) 

            return mem[i]

        mem = {}
        return dp (max_num)

    # Bottom up
    # def deleteAndEarn(self, nums: List[int]) -> int:
    #     cost_per_num = defaultdict(int)
    #     max_num = nums[0]
    #     for num in nums:
    #         cost_per_num[num] += num
    #         max_num = max(max_num, num)

    #     max_points = [0] * (max_num + 1)
    #     max_points[1] = cost_per_num[1]
    #     for i in range(2, max_num + 1):
    #         max_points[i] = max(max_points[i-1], max_points[i-2] + cost_per_num[i])

    #     return max_points[-1]
        


        