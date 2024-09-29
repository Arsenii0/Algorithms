invalid_node = -1
invalid_index = -1

from array import array
import math


def rangeIncludingEnd(start, end):
    return range(start, end + 1)


class MaxHeap:
    def __init__(self, arr):
        self.array = arr

    @staticmethod
    def heapHeight(arr):
        array_len = len(arr)
        log2_value = math.log2(array_len + 1)
        return math.ceil(log2_value) - 1

    @staticmethod
    def isMaxHeap(arr):
        for i in range(int((len(arr) - 2) / 2) + 1):

            # If left child is greater,
            # return false
            if arr[2 * i + 1] >= arr[i]:
                return False

            # If right child is greater,
            # return false
            if 2 * i + 2 < len(arr) and arr[2 * i + 2] >= arr[i]:
                return False

        return True

    @staticmethod
    def get_parent_node(array, index):
        if len(array) == 0:
            return invalid_node, invalid_index
        index = math.floor((index - 1) / 2)
        return array[index], index

    @staticmethod
    def get_left_node(array, index):
        return array[2 * index + 1]

    @staticmethod
    def get_right_node(array, index):
        return array[2 * index + 2]

    def insertNode(self, Node):
        # Step 1: Insert the new element at the end.
        # Step 2: Heapify the new element following bottom-up
        # approach. (Here we have iterative approach)
        self.array.append(Node)
        inserted_node_index = len(self.array) - 1
        while True:
            parent_node, parent_index = MaxHeap.get_parent_node(
                self.array, inserted_node_index
            )
            if parent_index == invalid_index:
                break
            if parent_node < Node:
                # swap
                self.array[parent_index] = Node
                self.array[inserted_node_index] = parent_node

                # go up
                inserted_node_index = parent_index
            else:
                break

    @staticmethod
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            MaxHeap.heapify(arr, n, largest)

    def printHeap(self):
        print(self.array)


def main():
    max_heap = MaxHeap([])
    for number in [1, 23, 12, 9, 30, 2, 50]:
        max_heap.insertNode(number)
    print(max_heap.array)
    print(MaxHeap.isMaxHeap(max_heap.array))

    n = len(max_heap.array)
    for index in range(n - 1, 0, -1):
        max_heap.array[index], max_heap.array[0] = (
            max_heap.array[0],
            max_heap.array[index],
        )  # swap
        MaxHeap.heapify(max_heap.array, index, 0)

    print(max_heap.array)


if __name__ == "__main__":
    main()
