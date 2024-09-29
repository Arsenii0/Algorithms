from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))

        if root is None:
            return True

        is_curr_balanced = abs(height(root.left) - height(root.right)) < 2
        if not is_curr_balanced:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
# Time complexity : O(nlogn)
# Space complexity : O(n). The recursion stack may contain all nodes if the tree is skewed.

def main():
    # Create the tree [1, null, 2, null, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    # Check if the tree is balanced
    solution = Solution()
    result = solution.isBalanced(root)
    print("Is the tree balanced?", result)

if __name__ == "__main__":
    main()
