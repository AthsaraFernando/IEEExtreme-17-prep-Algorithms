# Question

'''
Implement the merge sort algorithm in Python. Write a function merge_sort(arr) that take
s in an array arr and returns the sorted array using the merge sort algorithm.
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Test the function with a sample array
arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))  # Output: [5, 6, 7, 11, 12, 13]


