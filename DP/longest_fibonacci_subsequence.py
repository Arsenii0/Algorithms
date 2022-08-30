
# dp[i] = k
# k - the maximum fibonacci subsequence on i-th position

# Note - here I am striving to optimize from 2^n to n^2
def lenLongestFibSubseq_Tabulation(arr):
    # Because the single element is a fibonacci subsequence with the size = 1
    # Base condition
    dp = [1] * len(arr)
    
    for i in range (2, len(arr)):
        for j in range (0, i):
            if arr[i] == arr[i-1] + arr[i-2]:
                dp[i] = max(dp[i], dp[j] + 1)
            
    return max(dp)
    

def main():
    arr = [1,2,3,4,5,6,7,8]
    result = lenLongestFibSubseq_Tabulation(arr)
    
    print(result)

# Example 1:
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

# Example 2:
# Input: arr = [1,3,7,11,12,14,18]
# Output: 3
# Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].


if __name__ == "__main__":
    main()