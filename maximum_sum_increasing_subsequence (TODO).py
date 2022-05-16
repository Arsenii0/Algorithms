# Given an array of n positive integers. Find the sum of the maximum sum subsequence of
# the given array such that the integers in the subsequence are sorted in
# increasing order i.e. increasing subsequence.


class DP_ELEM:
    def __init__(self, increasing_subsequence_size, max_sum):
        self.subseq_size = increasing_subsequence_size
        self.max_sum = max_sum


# TODO, it doesn't work!!!
def maxSumIS(arr):
    result = None

    size = len(array)

    # 1 because each element is a single subsequence
    DP = []
    for i in range(0, len(arr)):
        DP.append(DP_ELEM(1, arr[i]))

    i = 0

    while i < size - 1:
        j = i + 1
        while j < size:
            if array[j] > array[i] and DP[j].subseq_size <= DP[i].subseq_size:
                DP[j].subseq_size += 1
                DP[j].max_sum += array[i]
            j += 1

        i += 1

    max_dp_elem = max(DP, key=lambda dp_elep: dp_elep.max_sum)
    return max_dp_elem.max_sum


# Test
# array = [1, 101, 2, 3, 100, 4, 5]
array = [27, 39, 22, 35, 3, 38, 48, 4, 19]

print(maxSumIS(array))
