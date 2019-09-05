def url(string, length):
    i = 0
    finalString = ''
    while i < length:
        if string[i] == ' ':
            finalString += '%20'
        else:
            finalString += string[i]
        i += 1
    return finalString


def findDiff(s, t):
    sL = list(s)
    tL = list(t)
    for i in s:
        tL.remove(i)
    return tL[0]


def plusOne(digits):

    return digits[0:len(digits)-1] + [digits[-1] + 1]


ls = 81924714791274897124978491
print(ls)
