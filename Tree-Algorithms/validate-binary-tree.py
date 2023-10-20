# Question

'''
Given a binary tree, determine if it is a valid binary search tree (BST). Implement the algorithm in Python. 
Write a function is_valid_BST(root) that takes in the root of the binary tree and returns True if it is a valid BST, and False otherwise.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_BST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_BST(root.left, low, root.val) and
            is_valid_BST(root.right, root.val, high))

# Test the function with a sample tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_BST(root))  # Output: True





