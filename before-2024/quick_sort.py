import math


def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        # pivot_index - 1 and pivot_index + 1 because pivot is already sorted
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


# All the elements less than(or equal to) the pivot lie before
# it and the elements greater than it lie after the pivot
# pivot - the element at high position (but can be at any random position)
# Lomuto Partitioning - partition index, ALL SMALLER ELEMENTS THATN THE PIVOT
# SWAP WITH THE ELEMENT ON PARTITION INDEX. Them swap high with partition index
def partition(arr, low, high):
    pivot = arr[high]

    curr_index = low
    partition_index = low

    while curr_index < high:
        is_current_less = arr[curr_index] <= pivot

        if is_current_less:
            arr[curr_index], arr[partition_index] = (
                arr[partition_index],
                arr[curr_index],
            )
            partition_index += 1

        curr_index += 1

    arr[high], arr[partition_index] = (
        arr[partition_index],
        arr[high],
    )

    return partition_index


# full test

arr = [2, 1, 6, 10, 4, 13, 1, 3, 9, 15, 18, 7]
quickSort(arr, 0, len(arr) - 1)

print(arr)
