# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

        
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]  # only empty subset [] is here
        for num in nums:
            new_subsets = []
            for curr_subset in results:
                temp = curr_subset.copy()
                temp.append(num)
                new_subsets.append(temp)
            results += new_subsets

        return results


