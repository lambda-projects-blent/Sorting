# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    indexA = 0
    indexB = 0
    for i in range(elements):
        if indexA >= len(arrA):
            merged_arr.extend(arrB[indexB:])
            break
        elif indexB >= len(arrB):
            merged_arr.extend(arrA[indexA:])
            break
        elif arrA[indexA] < arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1

    return merged_arr


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0: int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])

        arr = merge(left, right)
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(merge_sort(arr1))
