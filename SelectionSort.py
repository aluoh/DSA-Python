def selectionSort(a_list):
    # Iteration 1
    for start in range(len(a_list)):
        minpos = start  # Assume starting [0] is the smallest
        # Iteration 2
        for i in range(start, len(a_list)):
            if a_list[i] < a_list[minpos]:
                minpos = i
        # Swap
        temp = a_list[start]
        a_list[start] = a_list[minpos]
        a_list[minpos] = temp


# Worst Case: O(n²)
theList = [2, 5, 2, 1, 2, 12, 31, 24, 124, 12, 4]
selectionSort(theList)
print(theList)
