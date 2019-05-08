
# Implementation of Different Sorting Algorithms

from random import randint
import time

unsorted_list = []
for _ in range(1000):
    unsorted_list.append(randint(0, 10000))

# Bubble Sort

# O(N^2) since in reverse order we would perform n(n-1)/2 i.e. sum upto n-1
# Best Case is already sorted in which a single pass O(N) is required
# In-place implementation via all(), could have not in-place via sort() or sorted()
# Stable Sort


def bubble_sort(arr):

    while all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)) is False:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)


print(unsorted_list)
start = time.time()
bubble_sort(unsorted_list)
end = time.time()
print(end-start)


# Selection Sort

# While not needed as multiple passes over initial array not required
# O(N^2) complexity however since min does mean n(n-1)/2 operations
# Best Case still has us make (n-1) + (n-2) + .. + 1 = n(n-1)/2 comparisons : O(N^2)

def selection_sort(arr):

    for j in range(len(arr) - 1):
        arr[j], arr[arr.index(min(arr[j:]))] = arr[arr.index(min(arr[j:]))], arr[j]
    return print(arr)


start = time.time()
selection_sort(unsorted_list)
end = time.time()
print(end-start)


# Insertion Sort

# Use nested for loop which depends on outer index to move sorted/unsorted array boundary
# i defines boundary, j allows iteration through sorted array which increases by 1 on each pass

def insertion_sort(arr):

    for i in range(len(arr)-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)


start = time.time()
insertion_sort(unsorted_list)
end = time.time()
print(end-start)