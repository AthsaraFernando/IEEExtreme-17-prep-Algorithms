# Question

'''
Given an integer array, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum. 
Implement Kadane's algorithm in Python.
 Write a function max_subarray_sum(nums) that takes in an array nums and returns the maximum subarray sum.
'''

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function with a sample array
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6


