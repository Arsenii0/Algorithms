class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Level order traversal of a tree is BFS
# Pre-ordert, in-order, post-order tee traversal is DFS
def height_BFS(root):
    if root is None:
        return 0
    
    queue = []
    
    current = root
    queue.append(current)
    
    height = 1
    
    the_same_level_size = 0
    while len(queue) != 0:
        local_root = queue.pop(0)
        
        if the_same_level_size != 0:
            the_same_level_size -= 1
        
        if local_root.left:
            queue.append(local_root.left)
            
        if local_root.right:
            queue.append(local_root.right)
            
        if the_same_level_size == 0 and len(queue) != 0:
            height += 1
            the_same_level_size = len(queue)
            
    return height

def height_DFS(root):
    if root == None:
        return 0
    
    left_count = 1 + height_DFS(root.left)
    
    right_count = 1 + height_DFS(root.right)
    
    return max(left_count, right_count)

root = Node(5)
root.left = Node(5)

root.left.left = Node(4)
root.left.right = Node(10)

root.left.left.right = Node(8)
root.left.right.left = Node(5)

root.left.left.right.right = Node(8)

print(height_BFS(root))