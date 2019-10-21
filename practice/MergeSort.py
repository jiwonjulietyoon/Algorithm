



'''
Merge two sorted arrays into one sorted array
'''

def merge(arr1, arr2):  # arr1 and arr2 are already sorted
    M, N = len(arr1), len(arr2)

    new = [0] * (M+N)

    i = j = k = 0

    while i < M and j < N:
        a, b = arr1[i], arr2[j]
        if a <= b:
            new[k] = a
            i += 1
        else:
            new[k] = b
            j += 1
        k += 1

    while i < M:
        new[k] = arr1[i]
        i += 1
        k += 1

    while j < N:
        new[k] = arr2[j]
        j += 1
        k += 1

    return new

# a1 = [1, 5, 9, 10, 15]
# a2 = [1, 3, 13]
#
# print(merge(a1, a2))



def mergeSort(arr):
    N = len(arr)

    if N <= 1:
        return arr

    # 1. DIVIDE: recursively, until each sub-list only has 1 element
    mid = N // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)


    # 2. MERGE
    return merge(left, right)


a = [3, 7, 11, 2, 5, 1, 8, 4, 10]

print(mergeSort(a))