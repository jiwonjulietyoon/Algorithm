# Sort





#################################
# Quick Sort => taking the last item as the pivot

def partition(arr, l, r):  # l: index of leftmost element / r: index of rightmost element
    i = l-1  # index of smaller element
    p = arr[r]   # pivot is the last element

    for j in range(l, r):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1


def quickSort(arr, l, r):  # l: index of leftmost element / r: index of rightmost element
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr = [11, 45, 23, 81, 28, 34]
N = len(arr)

quickSort(arr, 0, N-1)

print(*arr)

