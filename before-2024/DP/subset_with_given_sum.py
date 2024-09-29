# Note! - this is only non-negative

def isSubsetSum(N, arr, sum):
    # Base Condition
    if sum == 0:
        return True
    if N == 0:
        return False

    # Recursion Logic/Recurrence Relation.
    if arr[N-1] > sum:
        return isSubsetSum(N-1, arr, sum)

    # here we check whether subset exists INCLUDING the last element
    # (because we substract it from the target sum)
    is_subset_including_last = isSubsetSum(N-1, arr, sum - arr[N-1])
    
    # here we check whether subset exists EXCLUDING the last element
    # (because we don't take it into account for the target sum)
    is_subset_excluding_last = isSubsetSum(N-1, arr, sum)
    
    return is_subset_excluding_last or is_subset_including_last

def isSubsetSum_MemorizationDP(N, arr, sum, dp):
    # Base Conditions
    
    # 1. n this case no matter what the given set is, 
    # one would always be able to find a subset (which is null set)
    if sum == 0:
        return True
    
    # 2. no matter how hard you we try, we won’t be able to get a subset
    # such that the sum of elements is equal to target sum S
    if N == 0:
        return False
    
    if dp[N][sum] != -1:
        return dp[N][sum]

    # Recursion Logic/Recurrence Relation.
    if arr[N-1] > sum:
        is_subset_sum = isSubsetSum_MemorizationDP(N-1, arr, sum, dp)
        dp[N][sum] = is_subset_sum
        return is_subset_sum

    # here we check whether subset exists INCLUDING the last element
    # (because we substract it from the target sum)
    is_subset_including_last = isSubsetSum_MemorizationDP(N-1, arr, sum - arr[N-1], dp)
    
    # here we check whether subset exists EXCLUDING the last element
    # (because we don't take it into account for the target sum)
    is_subset_excluding_last = isSubsetSum_MemorizationDP(N-1, arr, sum, dp)
    
    dp[N][sum] = is_subset_excluding_last or is_subset_including_last
    
    return dp[N][sum]


def isSubsetSum_TabulationDP(N, arr, sum):
    dp = [[-1 for i in range (sum + 1)] for j in range(N+1)]
    
    # Base Conditions
    for i in range(N+1):
        dp[i][0] = True
    for target_sum in range(sum + 1):
        dp[0][target_sum] = False
    
    for i in range (1, N+1):
        for target_sum in range(1, sum + 1):
            if target_sum < arr[i-1]:
                # do not take into account arr[i-1]
                dp[i][target_sum] = dp[i-1][target_sum]
            else:
                dp[i][target_sum] = dp[i-1][target_sum] or dp[i-1][target_sum - arr[i-1]]
    
    return dp[N][sum]

arr = [3, 34, 4, 12, 5, 2]
N = len(arr)
sum = 13

# + 1 because you need to handle sum 9 (but not 8)
dp = [[-1 for i in range (sum + 1)] for j in range(N+1)]

print(isSubsetSum_TabulationDP(N, arr, sum))
# Output: 1
# Explanation: Here there exists a subset with
# sum = 9, 4+3+2 = 9.
