# Question

'''
Given a directed graph, determine whether it contains any cycle. Implement a Python function is_cyclic(graph) that takes
 in a directed graph represented as an adjacency list and returns True if the graph contains a cycle, and False otherwise.
'''

def is_cyclic(graph):
    visited = set()
    rec_stack = set()
    cycle = []

    def dfs(node, path):
        if node in rec_stack:
            return True, path + [node]
        if node in visited:
            return False, path

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            has_cycle, cycle_path = dfs(neighbor, path + [node])
            if has_cycle:
                return True, cycle_path

        rec_stack.remove(node)
        return False, path

    for node in graph:
        has_cycle, cycle_path = dfs(node, [])
        if has_cycle:
            print("Cycle Found:", " -> ".join(cycle_path))
            return True
    return False

# Test the function with a sample graph
graph = {'A': ['B', 'C'],
         'B': ['A','D'],
         'C': ['E'],
         'D': ['C'],
         'E': []}

print(is_cyclic(graph))  # Output: True
