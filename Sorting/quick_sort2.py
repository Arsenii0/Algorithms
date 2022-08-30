import math

def quickSort_Lomuto(arr,low,high):
    # Base condition
    if low >= high:
        return
    
    # Recurrence logic
    partition_index = partition_Lomuto(arr, low, high)
    
    # +-1 is because the element on partition index is
    # already sorted
    quickSort_Lomuto(arr, low, partition_index - 1)
    quickSort_Lomuto(arr, partition_index + 1, high)
    
#             j [p]
# 4 1 3 9 7 8 5  6
#       i

# HINT: the bigger elements should go as much forward as possible
# That it why WE DO NOT SWAP it right away and wait the next smaller element

# It is Lomuto partitioning. 
# This works by iterating over the input array, swapping elements that are strictly
# less than a pre-selected pivot element
def partition_Lomuto(arr,low,high):
    pivot = arr[high]
    left_wall = low
    # one index (j) iterates over all elements
    # another (left-wall) - just swaps if less than the pivot
    for j in range (low, high):
        if arr[j] < pivot:
            arr[left_wall], arr[j] = arr[j], arr[left_wall]
            left_wall += 1
            
    partition_index = left_wall
    arr[partition_index], arr[high] = arr[high], arr[partition_index]
    return partition_index




def quickSort_Hoare(arr,low,high):
    # Base condition
    if low >= high:
        return
    
    # Recurrence logic
    partition_index = partition_Hoare(arr, low, high)
    
    # including partition_index because the element
    # on the partition index is NOT sorted
    quickSort_Hoare(arr, low, partition_index)
    quickSort_Hoare(arr, partition_index + 1, high)

# I find the Hoare scheme the easiest to understand, and it is also the most efficient. 
# It works by looking for the leftmost array item that out of place because it is larger 
# than the pivot, and the rightmost array item that is out of place because it is smaller 
# than the pivot. It swaps these, and then proceeds until the array has been properly 
# partitioned. That's really all there is to it.

# the pivot and elements equal to the pivot can end up anywhere within the partition after a partition step

# NOTE!!! We can take ANY element as pivot EXCEPT the last one. In this case
# left index could come to the end and we we will have recursion forever

# KEY POINTS:
# 1. Include partition index in quicksort because it is NOT on the right position
# 2. Partition index could be Any except the LAST one
# 3. left_pointer, right_pointer -> iterate and simply swap. That's it!


#
# 9,4,3,7,8,5,1,6
#
def partition_Hoare(arr,low,high):
    pivot_index = low
    
    pivot = arr[pivot_index]
    left_iter = low
    right_iter = high
    
    while left_iter < right_iter:
        while arr[left_iter] < pivot:
            left_iter += 1
        
        while arr[right_iter] > pivot:
            right_iter -= 1
        
        arr[left_iter], arr[right_iter] = arr[right_iter], arr[left_iter]
        
    return right_iter


N = 5
# arr = [9,4,3,7,8,5,1,6, 125125, 1245, 1222, 0, -11, 125, -11111, 1231, 33, 145215, 666, -123]
arr = [9,4,3,7,8,5,1,6]

low = 0
high = len(arr) - 1

quickSort_Hoare(arr, low, high)
print(arr)