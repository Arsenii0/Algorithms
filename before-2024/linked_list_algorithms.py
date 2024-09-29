class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    def appendNode(self, node):
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = node

    def printList(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def reverseList(self):
        curr = self.head
        prev = None
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def reverseListRecursive(self, head):
        if head is None or head.next is None:
            return head

        last_node = self.reverseListRecursive(head.next)

        # head.next is the last element (for each recursive method call: e.g 4,3,2,1)
        temp = head.next

        # temp is used ONLY between 2 Nodes (4 -> 3, 3 -> 2, 2 -> 1, 1 -> 0)
        temp.next = head
        temp.next.next = None

        return last_node


def sortedMerge(head1, head2):
    # first node is dummy
    sorted_merged = Node(0)
    tail = sorted_merged

    curr1 = head1
    curr2 = head2
    while (curr1.next is not None) and (curr2.next is not None):
        if curr1.data > curr2.data:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next

        tail = tail.next

    while curr1.next is not None:
        tail.next = curr1
        curr1 = curr1.next
        tail = tail.next

    while curr2.next is not None:
        tail.next = curr2
        curr2 = curr2.next
        tail = tail.next

    # return next because the first Node is dummy
    return sorted_merged.next


# Another solutions:
# 1. Add additional field "visited" to the node
# 2. Find lists count difference
# 3. Make circle in first list - and then need to do ... (some more staff you can think by yourself)
def findCommonNode(head1, head2):
    hash_table = {}

    iter1 = head1
    iter2 = head2

    while iter1 is not None:
        if iter1 in hash_table:
            return iter1

        hash_table[iter1] = 1
        iter1 = iter1.next

    while iter2 is not None:
        if iter2 in hash_table:
            return iter2

        hash_table[iter2] = 1
        iter2 = iter2.next


def test_find_common_node():
    linked_list1 = LinkedList(Node(0))
    linked_list1.appendNode(Node(1))
    linked_list1.appendNode(Node(2))

    common_node = Node(3)
    linked_list1.appendNode(common_node)
    linked_list1.appendNode(Node(4))

    linked_list2 = LinkedList(Node(5))
    linked_list2.appendNode(Node(6))
    linked_list2.appendNode(Node(7))
    linked_list2.appendNode(common_node)
    linked_list2.appendNode(Node(8))

    print(findCommonNode(linked_list1.head, linked_list2.head).data)


def test_reverse_list():
    linked_list = LinkedList(Node(0))
    linked_list.appendNode(Node(1))
    linked_list.appendNode(Node(2))
    linked_list.appendNode(Node(3))
    linked_list.appendNode(Node(4))

    linked_list.printList()

    print("reversed list:")
    linked_list.reverseList()
    linked_list.printList()


def test_merge_sorted_lists():
    linked_list1 = LinkedList(Node(20))
    linked_list1.appendNode(Node(28))
    linked_list1.appendNode(Node(58))
    linked_list1.appendNode(Node(100))

    linked_list2 = LinkedList(Node(22))
    linked_list2.appendNode(Node(44))
    linked_list2.appendNode(Node(55))
    linked_list2.appendNode(Node(67))

    LinkedList(sortedMerge(linked_list1.head, linked_list2.head)).printList()


def main():
    # test_reverse_list()
    # test_merge_sorted_lists()
    test_find_common_node()


if __name__ == "__main__":
    main()
