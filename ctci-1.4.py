def checkPalindrome(string):
    i = 0
    j = len(string)-1
    while i < len(string)-1 and j > -1:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def getPermutations(string):
    listOfPerm = []
    for i in range(len(string)):
        word = string[i:i+len(string)]
        if checkPalindrome(word):
            listOfPerm.append(word)
    return listOfPerm


print(getPermutations('Tact Coa'))
