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
    
    
# NOT CORRECT APPROACH BELOW!

# duplicates in binary search tree are not allowed
# def is_bst(root):
#     if root == None:
#         return False
    
#     left_subtree_bst = True
#     right_subtree_bst = True
    
#     if root.left != None:
#         if root.data <= root.left.data:
#             return False
#         else:
#             left_subtree_bst = is_bst(root.left)
    
#     if root.right != None:
#         if root.data >= root.right.data:
#             return False
#         else:
#             right_subtree_bst = is_bst(root.right)
    
#     return left_subtree_bst and right_subtree_bst
    

# Not BST
# root = Node(5)
# root.left = Node(4)
# root.right = Node(6)
# root.right.left = Node(3)
# root.right.right = Node(7)

# Is BST
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(is_bst(root))
