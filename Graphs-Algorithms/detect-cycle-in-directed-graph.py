# Question

'''
Given a directed graph, determine whether it contains any cycle. Implement a Python function is_cyclic(graph) that takes
 in a directed graph represented as an adjacency list and returns True if the graph contains a cycle, and False otherwise.
'''

def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    return False

# Test the function with a sample graph
graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['E'],
         'D': ['C'],
         'E': []}

print(is_cyclic(graph))  # Output: True


