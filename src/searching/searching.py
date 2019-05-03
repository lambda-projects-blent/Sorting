# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = int(len(arr)-1)

    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[int(mid)]
        if guess == target:
            return (mid, guess)
        elif target < arr[int(mid)]:
            high = int(mid - 1)
        else:
            low = int(mid + 1)

    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty


arr1 = [55, 44, 33, 3, 6, 7, 7, 8, 9, 2, 67, 89, 443,
        332, 78, 85, 443, 78, 44, 3, 28, 54, 37, 97, 35]

arr1.sort()

print(binary_search(arr1, 37))
