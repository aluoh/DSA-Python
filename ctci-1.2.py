def checkPermutation(string1, string2):
    l1 = sorted(string1)
    l2 = sorted(string2)
    return l1 == l2


def checkPermutation2(string1, string2):
    if len(string1) != len(string2):
        return False
    newL = []
    for i in string1:
        newL.append(i)
    for j in string2:
        newL.remove(j)
    return not newL


print(checkPermutation2('god', 'dog'))
