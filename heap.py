# A Binary Heap is a Binary Tree with following properties.
# 1. It’s a complete tree (All levels are completely filled except
#    possibly the last level and the last level has all keys as left as possible).
#
#   !!! This property of Binary Heap makes them suitable to be stored in an array. !!!

# 2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be
#    minimum among all keys present in Binary Heap. The same property must be recursively true
#    for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

invalid_node = -1
invalid_index = -1

import math


def rangeIncludingEnd(start, end):
    return range(start, end + 1)


class MinHeap:
    def __init__(self, arr):
        self.array = arr

    @staticmethod
    def heapHeight(arr):
        array_len = len(arr)
        log2_value = math.log2(array_len + 1)
        return math.ceil(log2_value) - 1

    @staticmethod
    def isMaxHeap(arr):
        # It should be a complete tree (i.e. all levels except last should be full).
        # Every node’s value should be less than or equal to its child node (considering min-heap).

        # Arsen's implementation
        heap_height = MinHeap.heapHeight(arr)
        if heap_height < 0:
            return False
        if heap_height == 0:
            return True

        current_heap_heigth = 1
        for current_index in rangeIncludingEnd(1, len(arr) - 1):
            is_on_right_node = True if current_index % 2 == 0 else False
            _, parent_index = MinHeap.get_parent_node(arr, current_index)

            if arr[current_index] >= arr[parent_index]:
                return False

            current_index += 1

        # Simplified implementation

        # for i in range(int((len(arr) - 2) / 2) + 1):

        #     # If left child is greater,
        #     # return false
        #     if arr[2 * i + 1] > arr[i]:
        #         return False

        #     # If right child is greater,
        #     # return false
        #     if 2 * i + 2 < len(arr) and arr[2 * i + 2] > arr[i]:
        #         return False

        return True

    @staticmethod
    def isMinHeap(arr):
        for i in range(int((len(arr) - 2) / 2) + 1):

            # If left child is greater,
            # return false
            if arr[2 * i + 1] <= arr[i]:
                return False

            # If right child is greater,
            # return false
            if 2 * i + 2 < len(arr) and arr[2 * i + 2] <= arr[i]:
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
        # approach.
        self.array.append(Node)
        inserted_node_index = len(self.array) - 1
        while True:
            parent_node, parent_index = MinHeap.get_parent_node(
                self.array, inserted_node_index
            )
            if parent_index == invalid_index:
                break
            if parent_node > Node:
                # swap
                self.array[parent_index] = Node
                self.array[inserted_node_index] = parent_node

                # go up
                inserted_node_index = parent_index
            else:
                break

    def printHeap(self):
        print(self.array)


def test_heap():
    min_heap = MinHeap([])

    min_heap.insertNode(17)
    min_heap.insertNode(27)
    min_heap.insertNode(19)
    min_heap.insertNode(21)
    min_heap.insertNode(33)
    min_heap.insertNode(14)
    min_heap.insertNode(5)
    min_heap.insertNode(9)
    min_heap.insertNode(11)
    min_heap.insertNode(18)

    heap_arr = [5, 9, 14, 11, 18, 19, 17, 27, 21, 33]
    print(MinHeap.isMinHeap(heap_arr))


def main():
    test_heap()


if __name__ == "__main__":
    main()
