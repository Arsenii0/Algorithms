class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root, l=None, r=None):
    pass


class Tree:
    def __init__(self, root):
        self.root = root

    def appendNode(self, node):
        current_tree_node = self.root
        while True:
            if current_tree_node.data >= node.data:
                if current_tree_node.left is not None:
                    current_tree_node = current_tree_node.left
                else:
                    current_tree_node.left = node
                    break
            else:
                if current_tree_node.right is not None:
                    current_tree_node = current_tree_node.right
                else:
                    current_tree_node.right = node
                    break

    def printTree(self):
        def printLocal(node):

            # this is in-order traversal: print in the middle
            # pre-order - print at the beginning
            # post-order - print at the end
            if node.left is not None:
                printLocal(node.left)
            print(node.data)
            if node.right is not None:
                printLocal(node.right)

        current_node = self.root
        printLocal(current_node)

    def search(self, key):
        root = self.root

        def localRecursionSearch(root, key):
            # Base Cases: root is null or key is present at root
            if root is None or root.data == key:
                return root

            # Key is greater than root's key
            if root.data < key:
                return localRecursionSearch(root.right, key)

            # Key is smaller than root's key
            return localRecursionSearch(root.left, key)

        return localRecursionSearch(root, key)

    # In Binary Tree, Inorder successor of a node is the next
    # node in Inorder traversal of the Binary Tree

    class NodeWrapper:
        def __init__(self, node):
            self.node = node

    # Inorder Successor is NULL for the last node in Inorder traversal
    # Did by myself - well done!
    def inOrderSuccessorUsingInorderTraversal(self, root, x):
        found_node = self.NodeWrapper(Node(-111111111111))

        def inorder_traverse_recursive(current_node, original_node_value, found_node):
            if current_node.left is not None:
                inorder_traverse_recursive(
                    current_node.left, original_node_value, found_node
                )

            if found_node.node.data < current_node.data:
                if (
                    found_node.node.data - original_node_value
                    > current_node.data - original_node_value
                    or found_node.node.data == original_node_value
                ):
                    found_node.node = current_node

            if current_node.right is not None:
                inorder_traverse_recursive(
                    current_node.right, original_node_value, found_node
                )

        found_node.node = x
        current_node = root

        # x = a if True else b

        inorder_traverse_recursive(root, found_node.node.data, found_node)
        return None if found_node.node == x else found_node.node

    def inOrderSuccessorMethod2(self, root, n):
        pass

    # Given a non-empty binary search tree,
    # return the minimum data value
    # found in that tree. Note that the
    # entire tree doesn't need to be searched
    def minValue(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current is not None:
            if current.left is None:
                break
            current = current.left

        return current

    class NodeWithParent:
        def __init__(self, node, node_parent):
            self.node = node
            self.node_parent = node_parent

    def searchWithParent(self, key):
        root = self.root

        def localRecursionSearch(root, key, parent_node=None):
            # Base Cases: root is null or key is present at root
            if root is None or root.data == key:
                return self.NodeWithParent(root, parent_node)

            # Key is greater than root's key
            if root.data < key:
                return localRecursionSearch(root.right, key, root)

            # Key is smaller than root's key
            return localRecursionSearch(root.left, key, root)

        return localRecursionSearch(root, key)

    def deleteNode(self, value):
        root = self.root

        node_to_delete_with_parent = self.searchWithParent(value)
        node_to_delete = node_to_delete_with_parent.node
        parent_node_to_delete = node_to_delete_with_parent.node_parent

        if node_to_delete is None:
            return root

        # 1. Node to be deleted is the leaf
        if node_to_delete.left is None and node_to_delete.right is None:
            if parent_node_to_delete is None:  # tree consists of 1 element
                del self.root
                return None
            if parent_node_to_delete.left == node_to_delete:
                parent_node_to_delete.left = None
            elif parent_node_to_delete.right == node_to_delete:
                parent_node_to_delete.right = None
            del node_to_delete
            return root

        # 2. Node to be deleted has only one child. Copy the child to the node and delete the child
        if node_to_delete.left is None and node_to_delete.right is not None:
            node_to_delete.data = node_to_delete.right.data
            del node_to_delete.right
            return root
        if node_to_delete.left is not None and node_to_delete.right is None:
            node_to_delete.data = node_to_delete.left.data
            del node_to_delete.left
            return root

        # 3. Node to be deleted has two children. Copy contents of the inorder successor to the node and delete the inorder successor.
        # Note that inorder predecessor can also be used.
        inorder_successor = self.inOrderSuccessorUsingInorderTraversal(
            root, node_to_delete
        )

        inorder_successor_parent = self.searchWithParent(
            inorder_successor.data
        ).node_parent

        # In 3-rd case, we need to copy inorder_successor value and delete it
        node_to_delete.data = inorder_successor.data

        if inorder_successor_parent.left == inorder_successor:
            inorder_successor_parent.left = None
        elif inorder_successor_parent.right == inorder_successor:
            inorder_successor_parent.right = None

        del inorder_successor
        return root


def test_is_BST():
    tree = Tree(Node(13))
    tree.appendNode(Node(5))
    tree.appendNode(Node(20))
    tree.appendNode(Node(11))
    tree.appendNode(Node(25))

    print(isBST(tree.root))


def test_find_inorder_successor():
    to_find = Node(14)
    tree = Tree(Node(20))
    tree.appendNode(Node(8))
    tree.appendNode(Node(22))
    tree.appendNode(Node(4))
    tree.appendNode(Node(12))
    tree.appendNode(Node(10))
    tree.appendNode(to_find)

    print(tree.inOrderSuccessorUsingInorderTraversal(tree.root, to_find).data)


def test_delete_node():
    tree = Tree(Node(50))
    tree.appendNode(Node(30))
    tree.appendNode(Node(70))
    tree.appendNode(Node(20))
    tree.appendNode(Node(40))
    tree.appendNode(Node(60))
    tree.appendNode(Node(80))

    tree.deleteNode(30)
    tree.printTree()


####################### 0. Inorder traversal ###############################
def inorderTraversal(root):
    if not root:
        return

    inorderTraversal(root.left)
    print(root.data)
    inorderTraversal(root.right)


####################### 1. Check if tree is symmetric ######################
def isTreeSymmetric(root):
    def isMirror(root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        if root1.data != root2.data:
            return False

        return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

    if not root:
        return True

    return isMirror(root.left, root.right)


def test_is_tree_symmetric():
    tree = Tree(Node(50))
    tree.appendNode(Node(30))
    tree.appendNode(Node(70))

    print(isTreeSymmetric(tree.root))


####################### 2. Maximum Depth of a Tree #######################
def maxDepth(root):
    if not root:
        return -1

    if not root.left and not root.right:
        return 0

    if not root.left:
        return maxDepth(root.right) + 1
    elif not root.right:
        return maxDepth(root.left) + 1

    max_height = max(maxDepth(root.left), maxDepth(root.right)) + 1
    return max_height


def test_calculate_tree_height():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(maxDepth(root))


####################### 3. Mirror the tree ###############################
def convertToMirrorTree(root):
    if not root:
        return root

    left_subtree = convertToMirrorTree(root.left)
    right_subtree = convertToMirrorTree(root.right)

    root.left = right_subtree
    root.right = left_subtree

    return root


def test_convert_to_mirror():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    convertToMirrorTree(root)

    inorderTraversal(root)


def main():
    test_convert_to_mirror()


if __name__ == "__main__":
    main()
