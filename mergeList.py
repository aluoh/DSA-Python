#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def degreeOfArray(arr):
    # Write your code here
    myDict = {}
    maxDegree = 1
    for i in range(len(arr)):
        if myDict.get(arr[i]) is not None:
            myDict[arr[i]] += 1
        else:
            myDict[arr[i]] = 1
    maxCounts = []
    singleCount = []
    maxCountsIndex = []
    for key, value in myDict.items():
        if myDict[key] > maxDegree:
            maxDegree = myDict[key]
            singleCount.append(key)
        else:
            maxCounts.append(key)
    if len(maxCounts) > 1:
        for i in maxCounts:
            maxCountsIndex.append(arr.index(i))
    return maxCountsIndex


arr = [1, 3, 2, 3]
print(degreeOfArray(arr))
