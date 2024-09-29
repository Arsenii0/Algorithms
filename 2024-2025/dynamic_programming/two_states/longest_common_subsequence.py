# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if (p1, p2) not in mem:
                # option 1: skip the element
                max_if_skip_element = dp(p1 + 1, p2)

                # option 2: include the element. 
                max_if_include_element = 0
                element = text1[p1]

                # find starting from the index p2
                position_in_text2 = text2.find(element, p2)
                if position_in_text2  != -1:
                    max_if_include_element = 1 + dp(p1 + 1, position_in_text2 + 1)
                else:
                    # do not +1 because not found in text2
                    max_if_include_element = dp(p1 + 1, p2)

                # choose the max from option1 and option2
                mem[(p1, p2)] = max(max_if_skip_element, max_if_include_element)

            return mem[(p1, p2)]

        mem = {}
        return dp(0,0)
    

# Complexity Analysis
# M = first string, N = second string

# Time complexity : O(M⋅N^2).

# The input parameters to the recursive function are a pair of integers; representing a position in each string. 
# There are M possible positions for the first string, and N for the second string. Therefore, this gives us M⋅N possible pairs of integers, and is the number of subproblems to be solved.

# Solving each subproblem requires, in the worst case, an O(N) operation; searching for a character 
# in a string of length N. This gives us a total of (M⋅N^2).

# Space complexity : O(M⋅N). (maxtrix)

# We need to store the answer for each of the M⋅N subproblems. Each subproblem takes O(1) space
# to store. This gives us a total of O(M⋅N).