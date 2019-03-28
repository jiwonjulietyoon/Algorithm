

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    return merge(left, right)


m = [5, 2, 1, 4, 5, 3, 2, 4, 6, 4, 9]

print(merge_sort(m))