# Example - Input:
# A[] = {2, 7, 6, 1, 4, 5}
# K = 3
# Output: 4
# Explanation:The subarray is {7, 6, 1, 4}
# with sum 18, which is divisible by 3.

# Solution (A, B, K - ints):
# A = K*B + mod(K) - it is intuitively understandable

# sum(i...0) = K*const1 + mod(sum_i / K)
# sum(j...0) = k*const2 + mod(sum_j / K)

# if mod(sum_i / K) == mod(sum_j / K) => sum(i...0) - sum(j...0) = K*const => so divisible by K


# int mod(a, b) {
#   c = a % b
#   return (c < 0) ? c + b : c
# }


def longestSubarraySumDivisibleByK(arr, k):
    mod_to_array_index_map = {}

    longest_subarray_size = 0
    sum_i = 0
    index = 0
    while index < len(arr):
        sum_i += arr[index]
        mod_i = sum_i % k

        if mod_i == 0:
            longest_subarray_size = index + 1

        if mod_i in mod_to_array_index_map.keys():
            distance = index - mod_to_array_index_map[mod_i]
            longest_subarray_size = max(longest_subarray_size, distance)
        else:
            mod_to_array_index_map[mod_i] = index

        index += 1

    return longest_subarray_size


def test_longestSubarraySumDivisibleByK():
    array = [1, 2, -2, 2, 2]
    K = 2

    print(longestSubarraySumDivisibleByK(array, K))

def main():
    test_longestSubarraySumDivisibleByK()


if __name__ == "__main__":
    main()
