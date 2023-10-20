# Question

'''
Given a tree, perform a depth-first search (DFS) traversal and return the nodes in the order they were visited.
 Implement the DFS algorithm in Python. Write a function dfs_traversal(root) that 
takes in the root of the tree and returns the DFS traversal of the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result

# Test the function with a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(dfs_traversal(root))  # Output: [1, 2, 4, 5, 3]




