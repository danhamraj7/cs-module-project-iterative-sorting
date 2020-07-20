def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # find the mid point.
    # Your code here
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low + high) // 2
    if target < arr[middle]:
        high = middle - 1  # this will elimate the RHS
    elif target > arr[middle]:
        low = middle + 1  # this will elimate LHS
    else:
        return middle

    return -1  # not found


# search 5

    # 0    1
    # |    |
    # [3,  5]

    # first mid point will be 3 check 5 against 3 it is not the target
    # so we toss out everything on the left we remain with five is the
    # mid point. mid point is +1 so the mid point will be 5
