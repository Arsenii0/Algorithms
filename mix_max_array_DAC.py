# Find min and max elements in the array using
# Divide And Conquer approach

import math


class Result:
    def __init__(self, min, max):
        self.min = min
        self.max = max


min_elem = None
max_elem = None


def find_min_max(array, start_index, end_index):
    size = end_index - start_index

    if size == 0:
        return Result(array[start_index], array[start_index])
    elif size == 1:
        if array[start_index] > array[end_index]:
            return Result(array[end_index], array[start_index])
        else:
            return Result(array[start_index], array[end_index])
    else:
        mid = start_index + math.floor((end_index - start_index) / 2)
        left_result = find_min_max(array, start_index, mid)
        right_result = find_min_max(array, mid + 1, end_index)

        min_elem = min(left_result.min, right_result.min)
        max_elem = max(left_result.max, right_result.max)

    return Result(min_elem, max_elem)


# Test
array = [3, 2, 1, 56, 10000, 167]
start = 0
end = len(array) - 1

result = find_min_max(array, start, end)
print(result.min, result.max)
