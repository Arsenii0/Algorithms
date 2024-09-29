

def merge(arr, l, m, r):
    sorted = []
    first_array_left = l
    second_array_left = m + 1
    
    while first_array_left <= m and second_array_left <= r:
        if arr[first_array_left] < arr[second_array_left]:
            sorted.append(arr[first_array_left])
            first_array_left+=1
        else:
            sorted.append(arr[second_array_left])
            second_array_left+=1
            
    while first_array_left <= m:
        sorted.append(arr[first_array_left])
        first_array_left+=1
        
    while second_array_left <= r:
        sorted.append(arr[second_array_left])
        second_array_left+=1
        
    for index in range(len(sorted)):
        arr[index+l] = sorted[index]


def mergeSort(arr, l, r):
    # Base condition
    if l >= r:
        return
    
    # Recursion Logic/Recurrence Relation
    mid = l + (r - l) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    
    merge(arr, l, mid, r)


N = 5
arr = [4,1,3,9,7]

left = 0
right = len(arr) - 1

mergeSort(arr, left, right)
print(arr)

# 1 3 4 7 9