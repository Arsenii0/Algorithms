class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Just use inordert traversal! And check that the array is sorted
nodes_list = []
def is_bst(root):
    if not root:
        return False
    
    left_subtree_bst = True
    right_subtree_bst = True
    
    if root.left != None:
        left_subtree_bst = is_bst(root.left)
        
    if len(nodes_list) != 0 and nodes_list[-1] >= root.data:
        return False
    
    nodes_list.append(root.data)
    
    if root.right != None:
        right_subtree_bst = is_bst(root.right)
        
    if not left_subtree_bst or not right_subtree_bst:
        return False
    
    return True

# Is BST
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(is_bst(root))
