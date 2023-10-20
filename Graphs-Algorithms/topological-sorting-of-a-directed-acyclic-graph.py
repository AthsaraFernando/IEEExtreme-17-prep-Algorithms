# Question

'''
Perform a topological sorting on a directed acyclic graph (DAG). Implement a Python function topological_sort(graph) 
that takes in a directed acyclic graph represented as an adjacency list and returns a topological ordering of the nodes.
'''

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.insert(0, node)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack

# Test the function with a sample graph
graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['D'],
         'D': ['E'],
         'E': []}

print(topological_sort(graph))  # Output: ['A', 'C', 'B', 'D', 'E']


