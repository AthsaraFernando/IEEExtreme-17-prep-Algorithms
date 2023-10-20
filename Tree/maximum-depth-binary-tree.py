# Question

'''
Given a binary tree, find its maximum depth. Implement the algorithm in Python. 
Write a function max_depth(root) that takes in the root of the binary tree and returns its maximum depth.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)

# Test the function with a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(max_depth(root))  # Output: 3






