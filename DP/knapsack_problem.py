
# Given two integer arrays val[0..N-1] and wt[0..N-1] which represent values
# and weights associated with N items respectively. Also given an
# integer W which represents knapsack capacity, find out the maximum
# value subset of val[] such that sum of the weights of this subset is smaller
# than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

def max_value_in_knapsack_recursive(N, values, weight, max_capacity):
    if max_capacity <= 0:
        return 0
    if N == 0:
        return 0

    # Recursion Logic/Recurrence Relation.
    if weight[N-1] > max_capacity:
        return max_value_in_knapsack_recursive(N-1, values, weight, max_capacity)

    # check knapsack capacity INCLUDING the last element
    result_including_last = values[N-1] + max_value_in_knapsack_recursive(N-1, values, weight, max_capacity - weight[N-1])
    
    # here we check whether subset exists EXCLUDING the last element
    # (because we don't take it into account for the target sum)
    result_excluding_last = max_value_in_knapsack_recursive(N-1, values, weight, max_capacity)
    
    return max(result_including_last, result_excluding_last)

# dp is 2 dimensional because we have 2 changed variables (N and max_capacity)
def dp_memorization_solution(values, weight, N, max_capacity, dp):
    
    # Base condition
    if max_capacity <= 0:
        return 0
    if N == 0:
        return 0
    
    if dp[N-1][max_capacity] != -1:
        return dp[N-1][max_capacity]

    # Recursion Logic/Recurrence Relation.
    if weight[N-1] > max_capacity:
        dp[N-1][max_capacity] = dp_memorization_solution(values, weight, N-1, max_capacity, dp)
        return dp[N-1][max_capacity]

    # check knapsack capacity INCLUDING the last element
    result_including_last = values[N-1] + dp_memorization_solution(values, weight, N-1, max_capacity - weight[N-1], dp)
    
    # here we check whether subset exists EXCLUDING the last element
    # (because we don't take it into account for the target sum)
    result_excluding_last = dp_memorization_solution(values, weight, N-1, max_capacity, dp)
    
    dp[N-1][max_capacity] = max(result_including_last, result_excluding_last)
    return dp[N-1][max_capacity]


# TODO ArsenP: doesn't work. Use memorization.
def dp_tabulation_solution(N, values, weight, max_capacity):
    if max_capacity <= 0:
        return 0
    if N == 0:
        return 0
    
    # The state DP[i][j] will denote maximum value 
    # of ‘j-weight’ considering all values from ‘1 to ith’. 
    dp = [[-1 for i in range(max_capacity + 1)] for j in range(N)]
    
    # Set initial conditions
    
    # Condition 1
    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0
    
    # Condition 2
    for capacity in range(0, max_capacity + 1):
        dp[0][capacity] = 0
    
    # Recurrence Relation
    for i in range (1, N):
        for capacity in range (max_capacity + 1):
            if capacity < weight[i-1]:
                dp[i][capacity] = dp[i-1][capacity]
            else:
                dp[i][capacity] = max(dp[i-1][capacity], dp[i-1][capacity] + values[i])

 
    return dp[N-1][max_capacity]




# Test
values = [60, 100, 120]
weight = [10, 20, 30]
max_capacity = 50
N = len(values)

dp = [[-1 for i in range(max_capacity + 1)] for j in range(N)]

# Memorization approach
result = dp_memorization_solution(values, weight, N, max_capacity, dp)

# tabulation approach (TODO ArsenP : doesn't work)
# result = dp_tabulation_solution(N, values, weight, max_capacity)

print(result)

# Output: 3