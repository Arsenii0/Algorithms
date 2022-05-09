
# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
# sequence such that all elements of the subsequence are sorted in increasing order.

# Input: arr[] = {3, 10, 2, 1, 20}
# Output: Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

def longestIncreasingSubsequence(array):
    arr_size = len(array)

    # 1 because 1 is also a subsequence
    # longest_increasing_subsq_sizes_on_each_array_position
    lis = [1] * arr_size
    maximum_subsq_size = 1

    i = 1

    while i < len(array):
        j = 0
        while j < i:
            if array[i] > array[j]:
                lis[i] = max(lis[i], lis[j] + 1) # +1 because single number is also a single subsequence
            j+=1
        i+=1

    return max(lis)

def main():
    arr = [3, 10, 2, 1, 20]

    # lis = [1, 1, 1, 1, 1]
    # if (arr[1] > arr[0]) -> lis[1] = max(lis[1], lis[0] + 1))
    # if (arr[2] > arr[0]) -> lis[2] = max(lis[2], lis[0] + 1))
    # if (arr[2] > arr[1]) -> lis[2] = max(lis[2], lis[1] + 1))

    # if (arr[3] > arr[0]) -> lis[3] = max(lis[3], lis[0] + 1))
    # if (arr[3] > arr[1]) -> lis[3] = max(lis[3], lis[1] + 1))
    # if (arr[3] > arr[2]) -> lis[3] = max(lis[3], lis[2] + 1))

    # if (arr[4] > arr[0]) -> lis[4] = max(lis[4], lis[0] + 1))
    # if (arr[4] > arr[1]) -> lis[4] = max(lis[4], lis[1] + 1))
    # if (arr[4] > arr[2]) -> lis[4] = max(lis[4], lis[2] + 1))
    # if (arr[4] > arr[3]) -> lis[4] = max(lis[4], lis[3] + 1))

    print(longestIncreasingSubsequence(arr))


if __name__ == "__main__":
    main()
