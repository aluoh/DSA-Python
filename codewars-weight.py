def order_weight(string):
    myDict = {}
    myList = string.split()
    print(myList)
    currSum = 0
    counter = 0
    ans = ""
    for i in string:
        if i == " ":
            myDict[currSum] = myList[counter]
            counter += 1
            currSum = 0
        else:
            currSum += int(i)
        # your code
    myList = []
    for theSum, theString in myDict.items():
        myList.append(theSum)
    myList.sort()
    for i in myList:
        ans += str(myDict.get(i)) + " "
    return ans.rstrip()


print(order_weight("103 123 4444 99 2000"))
