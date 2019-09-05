def isUnique(string):
    listCheck = []
    for i in string:
        if i in listCheck:
            return False
        else:
            listCheck.append(i)
    return True


def uniqueInPlace(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


print(uniqueInPlace('abcaad'))
