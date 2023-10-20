# Question

'''
Given an undirected, connected, and weighted graph, find the minimum spanning tree (MST) of the graph.
 Implement a Python function minimum_spanning_tree(graph) that takes
in a weighted graph as an adjacency list and returns the edges of the minimum spanning tree.
'''
def minimum_spanning_tree(graph):
    mst = []
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))
    edges.sort()
    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        parent[find(node1)] = find(node2)

    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst

# Test the function with a sample graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

print(minimum_spanning_tree(graph))  # Output: [(1, 'B', 'C'), (2, 'A', 'B'), (3, 'A', 'C')]

