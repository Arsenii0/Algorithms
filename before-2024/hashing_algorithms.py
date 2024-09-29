def hasArrayTwoNumbersWithExpectedSum(array, number_of_elements, expected_sum):

    hash_table = {}

    # hash_table: 9 - True(1), 8 - True(1), 6 - True(1), 7 - True(1), 4 - True(1)
    # array:      1, 2, 4, 3, 6

    result = []

    found = False
    for number in array:
        if number in hash_table:
            found = True
            result.append({number, expected_sum - number})

        hash_table[expected_sum - number] = 1

    return found, result


# The same task as above, but array is sorted. Hash table is not required

# Given a sorted array and a number x, find the pair in array whose sum is closest to x
# two pointer technique. ONLY WORKS WHEN ARRAY is SORTED!
def isPairSum(A, N, X):
    # represents first pointer
    i = 0

    # represents second pointer
    j = N - 1

    while i < j:

        # If we find a pair
        if A[i] + A[j] == X:
            return True

        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif A[i] + A[j] < X:
            i += 1

        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return 0


def testHasArrayTwoNumbersWithExpectedSum():
    number_of_elements = 5
    expected_sum = 10
    array = [1, 2, 4, 3, 7]

    found, result = hasArrayTwoNumbersWithExpectedSum(
        array, number_of_elements, expected_sum
    )
    for value in result:
        print(value)


def main():
    testHasArrayTwoNumbersWithExpectedSum()


if __name__ == "__main__":
    main()
