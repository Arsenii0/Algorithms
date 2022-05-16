import math

# Your Task:
# complete the function merge() which takes arr[], l, m, r as its input parameters and modifies
# arr[] in-place such that it is sorted from position l to position r, and
# function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.


# Merge arr[left:mid] and arr[mid+1:right] into a sorted array:
# 1. This method assumes that both arrays to merge are already sorted
# 2. Modifies arr[] in-place such that it is sorted from position l to position r
def merge(arr, left, mid, right):

    left_subarr = arr[left : mid + 1]  # mid + 1 in order to include mid
    right_subarr = arr[mid + 1 : right + 1]

    left_subarr_iter = 0
    right_subarr_iter = 0

    arr_iter = left

    while left_subarr_iter < len(left_subarr) and right_subarr_iter < len(right_subarr):
        if left_subarr[left_subarr_iter] > right_subarr[right_subarr_iter]:
            arr[arr_iter] = right_subarr[right_subarr_iter]
            right_subarr_iter += 1
        else:
            arr[arr_iter] = left_subarr[left_subarr_iter]
            left_subarr_iter += 1

        arr_iter += 1

    while left_subarr_iter < len(left_subarr):
        arr[arr_iter] = left_subarr[left_subarr_iter]
        left_subarr_iter += 1
        arr_iter += 1

    while right_subarr_iter < len(right_subarr):
        arr[arr_iter] = right_subarr[right_subarr_iter]
        right_subarr_iter += 1
        arr_iter += 1


def mergeSort(arr, left, right):
    distance = right - left

    if distance == 0:
        return  # because 1 element array is already sorted
    elif distance == 1:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

    else:
        mid = left + math.floor((right - left) / 2)
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# full test

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(arr, 0, len(arr) - 1)

print(arr)
