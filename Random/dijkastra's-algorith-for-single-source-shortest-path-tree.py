# Question

'''
Given a weighted graph and a source vertex, find the shortest paths from the source to all other vertices using Dijkstra's algorithm. 
Implement the algorithm in Python. Write a function dijkstra(graph, source) that takes in a graph represented as an 
adjacency list and a source vertex and returns the shortest paths to all other vertices from the source.
'''

import heapq
import math

def dijkstra(graph, source):
    distances = {node: math.inf for node in graph}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for (neighbor, weight) in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

# Test the function with a sample graph
graph = {'A': [('B', 2), ('C', 5)],
         'B': [('C', 1), ('D', 4)],
         'C': [('D', 2)],
         'D': []}

print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 2, 'C': 3, 'D': 5}



