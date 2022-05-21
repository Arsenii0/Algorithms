# Given an array of integers, find the length of the longest (strictly)
# increasing subsequence from the given array


def longestSubsequence(array):
    size = len(array)

    # 1 because each element is a single subsequence
    lis = [1] * size

    i = 0

    while i < size - 1:
        j = i + 1
        while j < size:
            if array[j] > array[i]:
                # increase by one only in case previous subsequence size is equal of bigger. The current (j)
                # element is bigger than (i) element and that's why the current subsequence increase by 1
                if lis[j] <= lis[i]:
                    lis[j] += 1
            j += 1

        i += 1

    return max(lis)


def longestSubsequence_AnotherApproach(array):
    size = len(array)

    # 1 because each element is a single subsequence
    lis = [1] * size

    i = 0

    for i in range(1, size):
        for j in range(0, i):
            if array[i] > array[j]:
                # +1 means including array[i] into the subsequence
                if lis[i] < lis[j] + 1:
                    lis[i] += 1

    return max(lis)


def main():
    array1 = [5, 8, 3, 7, 9, 1]
    # 5 7 9, with length 3
    print(longestSubsequence_AnotherApproach(array1))

    array2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # 0 2 6 9 13 15, which has length 6
    print(longestSubsequence(array2))

    array3 = [27, 39, 22, 35, 3, 38, 48, 4, 19]
    print(longestSubsequence(array3))


if __name__ == "__main__":
    main()
