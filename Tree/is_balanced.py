from tree_height import *

def is_balanced(root):
    if root is None:
        return True
    
    if abs(height_DFS(root.left) - height_DFS(root.right)) > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(is_balanced(root))