def h(nums):
    myDict = {}
    result = []

    for i in nums:
        myDict[i] = 1
        if -i in myDict:
            print(i)

    print(myDict)


(h([1, 1, 12, 1, 12, 1255, -12]))
