import math

# Your Task:
# complete the function merge() which takes arr[], l, m, r as its input parameters and modifies
# arr[] in-place such that it is sorted from position l to position r, and
# function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.


# Merge arr[left:mid] and arr[mid+1:right] into a sorted array:
# 1. This method assumes that both arrays to merge are already sorted
# 2. Modifies arr[] in-place such that it is sorted from position l to position r
def merge(arr, left, mid, right):

    arr_left = arr[left : mid + 1]
    arr_right = arr[mid + 1 : right + 1]

    left_iter = 0
    right_iter = 0

    distance = right - left

    while left_iter <= mid and right_iter <= right:
        if arr_left[left_iter] > arr_right[right_iter]:
            arr[left + left_iter] = arr_right[right_iter]
            right_iter += 1
        else:
            left_iter += 1

    while left_iter <= distance:
        arr[left_iter] = arr_right[left_iter]
        left_iter += 1

    while right_iter <= distance:
        arr[right_iter] = arr_right[right_iter]
        right_iter += 1


def mergeSort(arr, left, right):
    pass


# test merge
arr = [7, 8, 9, 11, 3, 6, 10]

start_index = 0
end_index = len(arr) - 1
merge(arr, start_index, math.floor(end_index / 2), end_index)

print(arr)


# full test

# arr = [4, 1, 3, 9, 7]
# mergeSort(arr, 0, len(arr) - 1)

# print(arr)
