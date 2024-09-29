class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(root):
    queue = []
    
    current = root
    queue.append(current)
    
    result = []
    while len(queue) != 0:
        local_root = queue.pop(0)
        result.append(local_root.data)
        
        if local_root.left:
            queue.append(local_root.left)
            
        if local_root.right:
            queue.append(local_root.right)
            
    return result

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(level_order_traversal(root))