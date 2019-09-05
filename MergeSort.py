def merge(left, right):
    (C, m, n) = ([], len(left), len(right))
    (i, j) = (0, 0)
    while i + j < m + n:
        if i == m:
            j += 1
        elif j == n:
            C.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            C.append(left[i])
            i += 1
        elif left[i] > right[j]:
            C.append(right[j])
            j += 1
    return C


def mergeSort(a_list, left, right):
    if right - left <= 1:
        return a_list[left:right]
    if right - left > 1:
        mid = (left + right) // 2
        newL = mergeSort(a_list, left, mid)
        newR = mergeSort(a_list, mid+1, right)
        return (merge(newL, newR))


unsortedList = list(range(0, 500))
revList = unsortedList[::-1]
newL = mergeSort(revList, 0, len(revList)-1)
print(newL)
