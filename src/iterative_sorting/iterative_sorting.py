# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for i in range(len(arr)):
        j = 0
        swap_occurred = False

        while j < len(arr) - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_occurred = True
            j += 1

        if swap_occurred is False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


print(bubble_sort(arr1))
