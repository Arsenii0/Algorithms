
# LCS = L(s1[0...s1_size], s2[0...s2_size])
# if the last character matches, then LCS = 1 + L(s1[0...s1_size - 1, s2[0...s2_size - 1]])
# else LCS = max (L(s1[0...s1_size - 1], s2[0...s2_size]), L(s1[0...s1_size], s2[0...s2_size-1]))

# because of the above explanation - we have an optimal substructure
# as the main problem can be solved using solutions to subproblems

# no DP approach
# def longest_common_subsequence(s1, s2, s1_size, s2_size):
#     if s1_size < 1 or s2_size < 1:
#         return 0
#     if s1[s1_size - 1] == s2[s2_size - 1]:
#         return 1 + longest_common_subsequence(s1, s2, s1_size - 1, s2_size - 1)
#     else:
#         return max(longest_common_subsequence(s1, s2, s1_size, s2_size - 1), longest_common_subsequence(s1, s2, s1_size - 1, s2_size - 0))





# DP approach (because we have overlapping subproblems)
def longest_common_subsequence_dp(s1, s2, s1_size, s2_size, dp):
    if s1_size < 1 or s2_size < 1:
        return 0

    if dp[s1_size][s2_size] != -1:
        return dp[s1_size][s2_size]

    if s1[s1_size - 1] == s2[s2_size - 1]:
        res = longest_common_subsequence_dp(s1, s2, s1_size - 1, s2_size - 1, dp)
        dp[s1_size][s2_size] = 1 + res
        
        return dp[s1_size][s2_size]

    res1 = longest_common_subsequence_dp(s1, s2, s1_size, s2_size - 1, dp)
    res2 = longest_common_subsequence_dp(s1, s2, s1_size - 1, s2_size, dp)
    dp[s1_size][s2_size] = max(res1, res2)
        
    return dp[s1_size][s2_size]


# Driver program to test the above function
X = "ABCDGH"
Y = "ACDGHR"

dp = [[-1 for i in range(len(Y) + 1)]for j in range(len(X) + 1)]

result = longest_common_subsequence_dp(X, Y, len(X), len(Y), dp)
print("Length of LCS is ", result)
