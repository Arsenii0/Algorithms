# Given an array of n positive integers. Find the sum of the maximum sum subsequence of
# the given array such that the integers in the subsequence are sorted in
# increasing order i.e. increasing subsequence.


# Note that the subsequence can be the longest - but the sum of this subsequence NOT the maximum
# Also consider the case 1: 1, 99, 2, 3, 4, 85, 100:
# longest subsequence -     1, 2, 3, 4, 100
# max sum -                 1, 99, 100 (however it is shorter)

# case 2:                   100, 1, 2, 3, 4, 5, 6
# longest subsequence -     1, 2, 3, 4, 5, 6
# max sum -                 100

# case 3:                   1, 101, 2, 3, 100, 4, 5,
# result:                   1 + 2 + 3 + 100
def maxSumIS(arr):
    size = len(arr)

    DP = []
    # 1 because each element is a single subsequence
    for i in range(0, len(arr)):
        DP.append(arr[i])

    i = 0

    for i in range(1, size):
        for j in range(i):
            if arr[i] > arr[j] and DP[i] < DP[j] + arr[i]:
                DP[i] = DP[j] + arr[i]

    return max(DP)


# Test
# array = [1, 101, 2, 3, 100, 4, 5]
array = [27, 39, 22, 35, 3, 38, 48, 4, 19]

print(maxSumIS(array))
