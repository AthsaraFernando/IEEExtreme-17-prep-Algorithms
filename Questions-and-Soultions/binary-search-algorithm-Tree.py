# Question

'''
You are given a sorted array of integers. Implement a Python function that searches for a specific target integer 
in the array using the binary search algorithm. Write a function binary_search(arr, target) that takes in a sorted array arr
and a target integer and returns the index of the target if it is found, or -1 if it is not found.
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test the function with a sample array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
print(binary_search(arr, target))  # Output: 5


