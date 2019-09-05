def insertionSort(a_list):

    for i in range(1, len(a_list)):
        j = i - 1
        while j >= 0 and a_list[i] < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = a_list[i]


the_list = [5, 512, 12, 31, 23, 12, 1, 25, 124]
print(the_list)
insertionSort(the_list)
print(the_list)
