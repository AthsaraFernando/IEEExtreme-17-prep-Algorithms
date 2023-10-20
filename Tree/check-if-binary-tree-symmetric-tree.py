# Question

'''
Given a binary tree, check whether it is a mirror of itself. Implement the algorithm in Python. 
Write a function is_symmetric(root) that takes in the root of
 the binary tree and returns True if the tree is symmetric, and False otherwise.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

    return is_mirror(root, root)

# Test the function with a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))  # Output: True




