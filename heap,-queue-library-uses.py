import heapq
import queue

# 1. Creating a min-heap with `heapq`.
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

# 2. Creating a max-heap with negated values using `heapq`.
max_heap = []
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -7)

# 3. Merging multiple sorted inputs with `heapq.merge`.
sorted1 = [1, 3, 5]
sorted2 = [2, 4, 6]
merged = heapq.merge(sorted1, sorted2)

# 4. Implementing priority queues with `queue.PriorityQueue`.
q = queue.PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

# 5. Using `heapq` to find the N smallest or largest items in a collection.
largest = heapq.nlargest(3, my_list)
smallest = heapq.nsmallest(3, my_list)

# 6. Using a priority queue for managing jobs and tasks.
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

# 7. Implementing a stack using `queue.LifoQueue`.
stack = queue.LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)

# 8. Implementing a FIFO queue using `queue.Queue`.
fifo_queue = queue.Queue()
fifo_queue.put(1)
fifo_queue.put(2)
fifo_queue.put(3)

# 9. Priority queue with a custom comparator function using `heapq`.
class CustomObject:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

# 10. Using `heapq` to merge K sorted arrays efficiently.
import itertools
merged_array = list(heapq.merge(*list_of_sorted_arrays))
