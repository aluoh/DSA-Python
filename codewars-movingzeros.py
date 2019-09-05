def move_zeros(array):
    for i in array:
        if type(i) != bool:
            if i == 0:
                num = int(i)
                array.pop(array.index(i))
                array.append(num)
    return array

# Alternative Solution


def move_zeros_2(array):
    i = 0
    j = 0
    while i < len(array):
        if array[i] != 0:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            j += 1
        i += 1
    return array


arr = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
ss = move_zeros_2(arr)
s = move_zeros(arr)

print(s)
print(ss)
