def diStringMatch(str):
    tracker = 0
    i = 0
    d = len(str)
    listOfAns = []
    while tracker < len(str):
        if str[tracker] == "I":
            listOfAns.append(i)
            i += 1
        elif str[tracker] == "D":
            listOfAns.append(d)
            d -= 1
        tracker += 1
    listOfAns.append(i)
    return listOfAns


print(diStringMatch("DIDIDIDIDIIIIDIIDDD"))
