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
            if array[j] > array[i] and lis[j] <= lis[i]:
                lis[j] += 1
            j += 1

        i += 1

    return max(lis)


def main():
    array1 = [5, 8, 3, 7, 9, 1]
    # 5 7 9, with length 3
    print(longestSubsequence(array1))

    array2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # 0 2 6 9 13 15, which has length 6
    print(longestSubsequence(array2))


if __name__ == "__main__":
    main()