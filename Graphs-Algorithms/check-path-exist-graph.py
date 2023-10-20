# Question

'''
You are given a list of edges that represent connections between nodes in a graph. 
Your task is to implement a Python function that can determine whether there exists a path between two given nodes in the graph.
 Write a function is_path_exists(edges, node1, node2) that takes in a list of edges, representing connections between nodes, and two nodes, node1 and node2,
 and returns True if there exists a path between the two nodes, and False otherwise.
'''

from collections import defaultdict

def is_path_exists(edges, node1, node2):
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        if node == node2:
            return True
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        return False

    return dfs(node1)

# Test the function with the given example
edges = [(1, 2), (2, 3), (3, 4), (2, 4), (4, 5)]
print(is_path_exists(edges, 1, 5))  # True
print(is_path_exists(edges, 1, 6))  # False
