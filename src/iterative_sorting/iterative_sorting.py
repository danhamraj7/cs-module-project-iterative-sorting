# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # loops through the whole arr
        cur_index = i  # this is the first index in the arr
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # iterate over the unsorted part of the array
        # find the index of the element with the smallest value
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
    arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # it repeats the loop until the entire arr is sorted
    # Your code here
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        # traverse the array
        # i starts with the first el,  -1 will stop i from comparing after it has loop through the entire arr
        for i in range(0, len(arr) - 1):
          # compares two elements in one go
            if arr[i] > arr[i + 1]:
                # swaps the elements if they are not in proper order
                arr[i], arr[i + 1], arr[i]
                swaps_occurred = True  # toggle swap

    return arr


print(bubble_sort([3, 5, 7, 1, 2, 9, 8, 4, 6]))


# bubble sort causes the big value elements to rise to the right side
# the first iteration the largest element in the arr goes to first
# on the right side
# on the 2nd iteration the 2nd largest goes second on the RHS


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
