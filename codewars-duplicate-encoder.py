def duplicate_encoder(word):
    mydict = {}
    lol = word.lower()
    finalString = ""
    for i in lol:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    for i in mydict:
        if mydict[i] > 1:
            mydict[i] = ')'
        else:
            mydict[i] = '('
    for i in lol:
        if i in mydict:
            finalString += mydict[i]
    return finalString


word = "abcdeeee"
letter = "e"
print(word.count(letter))
