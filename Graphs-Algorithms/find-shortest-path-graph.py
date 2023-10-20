# Question

'''
You are given a weighted graph and two nodes. Implement a Python function that finds the shortest path between the two given nodes.
 Write a function shortest_path(graph, start, end) that takes in a weighted graph,
 represented as an adjacency list, and two nodes, start and end, and returns the shortest path between the two nodes.
'''
import heapq

def shortest_path(graph, start, end):
    heap = [(0, start, [])]
    while heap:
        (cost, v, path) = heapq.heappop(heap)
        if v not in path:
            path = path + [v]
            if v == end:
                return path
            for (next_v, c) in graph.get(v, ()):
                heapq.heappush(heap, (cost + c, next_v, path))
    return []

# Test the function with a sample graph
graph = {'A': [('B', 2), ('C', 5)],
         'B': [('C', 6), ('D', 1)],
         'C': [('D', 2)],
         'D': [('E', 5)],
         'E': []}

print(shortest_path(graph, 'A', 'E'))  # Output: ['A', 'B', 'D', 'E']
