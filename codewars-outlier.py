def find_outlier(integers):
    evenCounter = 0
    oddCounter = 0
    for i in integers:
        if i % 2 != 0:
            oddCounter += 1
        else:
            evenCounter += 1
    for i in integers:
        if i % 2 == 0 and evenCounter == 1:
            return i
        if i % 2 != 0 and oddCounter == 1:
            return i
    return None


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
